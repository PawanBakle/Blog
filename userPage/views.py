from django.shortcuts import render,redirect
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
def Profile(request):
    if request.method == 'POST':
        u_form =  UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form =  UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form':u_form,'p_form':p_form}
    return render(request,'userPage/Profile.html',context)