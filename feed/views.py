from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from feed import models
from .forms import NewPost
from django.contrib.auth.admin import User

def home(request):
    posts = Posts.objects.all()
    context = {'post': posts}
    return render(request, 'feed/main.html', context)


def about(request):
    return render(request, 'feed/page.html')


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
    return render(request, 'feed/post_detail.html', context={"post_detail": user_post})
