from django.shortcuts import render,redirect
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
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
@login_required
def profile(request):
    return render(request,'userPage/profile.html')
def sign_out(request):
    logout(request)
    return redirect('login')
def Profile(request, pk):
    user = User.objects.get(id=pk)
    post = user.objects.get(filter = 'title')
    posts = user.objects.get(filter='content')
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST,instance=request.user)
        pform = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            return redirect('profile')
    else:
        uform = UserUpdateForm(instance=request.user)

    context = {'u_form':uform,'user':user,'post':post,'content':posts}
    return render(request,'userPage/Profile.html',context)
