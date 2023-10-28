from . import views
from django.urls import path
from django.http import HttpResponse
urlpatterns = [
path('', views.home,name='blog-home'),
path('about/', views.about,name = "about"),
path('new_post/', views.new_posts,name = "new-post"),
path('post_detail/<int:pk>/', views.post_detail,name ="details"),
path('user_page/', views.home,name ="userpage"),
    ]