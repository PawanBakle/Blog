from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts,Comments
from feed import models
from django.contrib.auth.models import User
from .forms import NewPost,Post_edit,Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User

def home(request):
    posts = Posts.objects.all()
    context = {'post': posts}
    return render(request, 'feed/main.html', context)


def about(request):
    return render(request, 'feed/page.html')


@login_required
def new_posts(request):
    if request.method == 'POST':
        post_form = NewPost(request.POST)
        if post_form.is_valid():
            new_blog = post_form.save(commit=False)
            new_blog.author = request.user  # Assign the currently logged-in user as the author
            new_blog.save()
            return redirect('/')
    else:
        post_form = NewPost(request.POST, instance=request.user)

    context = {'post_form': post_form}
    return render(request, 'feed/add_post.html', context)


def post_detail(request, pk):
    user_post = Posts.objects.get(id=pk)
    user_comments = Comments.objects.filter(posts = user_post)
    return render(request, 'feed/post_detail.html', context={"post_detail": user_post,'comments':user_comments})

@login_required
def post_edit(request, pk):
    post = Posts.objects.get(id = pk)
    if request.method == 'POST':
        edit = NewPost(request.POST,instance=post)
        if edit.is_valid():
            edit.save()
            return redirect('details',pk = post.id)
    else:
        edit = NewPost(instance=post)
    return render(request, 'feed/post_edit.html', context={"post":post,"post_edit": edit})

def post_delete(request, pk):
    post = Posts.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    context = {
        'post': post
    }
    return render(request, 'feed/post_delete.html', context)
def my_posts(request,username):
    user = User.objects.get(username= username)
    post = Posts.objects.filter(author = user)
    return render(request,'feed/post_delete.html',{'posts': post, 'user': user})
@login_required
def add_comment(request,pk):
    user_post = Posts.objects.get(id=pk)
    if request.method == 'POST':
        comment = Comment(request.POST)
        if comment.is_valid():
            
            com = comment.save(commit=False)
            com.u_name = request.user
            com.posts = user_post
            com.save()
            return redirect('/')
    else:
        comment = Comment(request.POST)
        
    return render(request,'feed/comment.html',{'comment':comment})