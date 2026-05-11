from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts,Comments,UserData
from feed import models
from django.contrib.auth.models import User
from .forms import NewPost,Post_edit,Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User
import json
from django.http import HttpResponseBadRequest, JsonResponse
from .adapter import normalize_reqres,fetch_data

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Posts, Comments, UserData
from .forms import NewPost, Comment
from .adapter import normalize_reqres, fetch_data


def get_api(request):
    """Fetch and store external API data"""
    data_fetch = fetch_data()
    data = normalize_reqres(data_fetch)

    # Only pass fields that exist in UserData model to avoid integrity errors
    
    allowed_fields = [f.name for f in UserData._meta.get_fields() if f.name != 'id']
    filtered_data = {k: v for k, v in data.items() if k in allowed_fields}
    
    user_data = UserData.objects.create(**filtered_data)
    all_data = UserData.objects.all()
    print(all_data)
    return render(request, 'feed/third_party.html', {'data': user_data})


def home(request):
    posts = Posts.objects.all()
    context = {'posts': posts}   
    return render(request, 'feed/main.html', context)


def home_by_tag(request, tag):
    """Filter posts by tag"""
    posts = Posts.objects.filter(tag=tag)
    return render(request, 'feed/main.html', {'posts': posts})


def about(request):
    return render(request, 'feed/page.html')



@login_required
def new_posts(request):
    """Create a new post"""
    if request.method == 'POST':
        post_form = NewPost(request.POST)
        if post_form.is_valid():
            new_blog = post_form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            return redirect('/')
    else:
        post_form = NewPost()
    context = {'post_form': post_form}
    return render(request, 'feed/add_post.html', context)


def post_detail(request, pk):
    """View a single post and its comments"""
    user_post = get_object_or_404(Posts, id=pk)
    user_comments = Comments.objects.filter(posts=user_post)
    return render(request, 'feed/post_detail.html', context={
        "user_post": user_post,
        'comments': user_comments
    })


@login_required
def post_edit(request, pk):
    """Edit an existing post - only author allowed"""
    post = get_object_or_404(Posts, id=pk)
    
    # Authorisation check
    if post.author != request.user:
        return redirect('home')  # or raise PermissionDenied
    
    if request.method == 'POST':
        edit = NewPost(request.POST, instance=post)
        if edit.is_valid():
            edit.save()
            return redirect('details', pk=post.id)
    else:
        edit = NewPost(instance=post)
    return render(request, 'feed/post_edit.html', context={
        "post": post,
        "post_edit": edit
    })


@login_required
def post_delete(request, pk):
    """Delete a post - only author allowed"""
    post = get_object_or_404(Posts, id=pk)
    
    if post.author != request.user:
        return redirect('home')
    
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    context = {'post': post}
    return render(request, 'feed/post_delete.html', context)



def my_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts = Posts.objects.filter(author=user)
    return render(request, 'feed/main.html', {'posts': posts})

@login_required
def add_comment(request, pk):
    """Add a comment to a post"""
    user_post = get_object_or_404(Posts, id=pk)
    
    if request.method == 'POST':
        comment = Comment(request.POST)
        if comment.is_valid():
            com = comment.save(commit=False)
            com.u_name = request.user
            com.posts = user_post
            com.save()
            # Redirect back to the post detail page
            return redirect('details', pk=user_post.id)
    else:
        comment = Comment()
    
    return render(request, 'feed/comment.html', {'comment': comment})

