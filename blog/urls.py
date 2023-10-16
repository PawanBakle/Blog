"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path,include
from django.http import HttpResponse
from userPage import views as user_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('feed.urls')),
    path('register/',user_view.register,name= "register-user"),
    path('sign_in/', user_view.sign_in, name="login"),
    path('sign_out/', user_view.sign_out, name="logout"),
    path('profile/', user_view.profile, name="profile"),

]
