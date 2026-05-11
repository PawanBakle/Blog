from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages


from feed.models import *
from .models import *

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.clean()
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'userPage/register.html', {'form':form})




def sign_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'userPage/login.html')

def sign_out(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')
@login_required
def profile(request, pk):
    # Only allow users to view their own profile (or admin)
    if request.user.id != pk:
        return redirect('blog-home')  # or raise PermissionDenied

    user = get_object_or_404(User, id=pk)
    my_post = Posts.objects.filter(author=user)

    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            return redirect('profile', pk=request.user.id)
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': uform,
        'p_form': pform,
        'my_post': my_post,
        'user': user,   
    }
    return render(request, 'userPage/Profile.html', context)
