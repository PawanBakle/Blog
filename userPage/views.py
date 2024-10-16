from django.shortcuts import render,redirect
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
        user = authenticate(request,username=username,password=password)
        login(request,user)
        return redirect('/')

    return render(request,'userPage/SignIn.html')


def sign_out(request):
    logout(request)
    return redirect('login')
def profile(request,pk):
    # my_post = Posts.objects.filter(request.user)
    # In your view
    # user_profile = Profile.objects.get(user=request.user)
    # user_post = Posts.objects.filter(author=user_profile.user)
    user = User.objects.get(id= pk)
    post = Posts.objects.filter(author = user)

    if request.method == 'POST':
        uform = UserUpdateForm(request.POST,instance=request.user)
        pform = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            return redirect('profile')
    else:
        uform = UserUpdateForm(instance=request.user)

    context = {'u_form':uform,'my_post':post,'user': user}
    return render(request,'userPage/Profile.html',context)
