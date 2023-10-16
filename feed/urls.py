from . import views
from django.urls import path
from django.http import HttpResponse
urlpatterns = [
path('', views.home,name='blog-home'),
path('about/', views.about,name = "about"),
    ]