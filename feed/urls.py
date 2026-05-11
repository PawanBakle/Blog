from . import views
from django.urls import path
from django.http import HttpResponse
urlpatterns = [
path('', views.home,name='blog-home'),
path('about/', views.about,name = "about"),
path('new_posts/', views.new_posts,name = "new_posts"),
path('user/<str:username>/', views.my_posts, name='my_posts'),
path('post_detail/<int:pk>/', views.post_detail,name ="details"),
path('edit/<int:pk>/', views.post_edit,name ="edit"),
path('post_delete/<int:pk>/', views.post_delete,name ="delete"),
path('user_page/', views.home,name ="userpage"),
path('add_comment/<int:pk>/', views.add_comment,name ="comment"),
path('home/tag/<str:tag>/', views.home_by_tag, name='home_by_tag'),
path('third_party/', views.get_api, name='third_party'),
    ]