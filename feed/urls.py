from . import views
from django.urls import path
from django.http import HttpResponse
urlpatterns = [
path('', views.home,name='blog-home'),
path('about/', views.about,name = "about"),
path('new_post/', views.new_posts,name = "new-post"),
path('post_detail/<int:pk>/', views.post_detail,name ="details"),
path('edit/<int:pk>/', views.post_edit,name ="edit"),
path('post_delete/<int:pk>/', views.post_delete,name ="delete"),
path('user_page/', views.home,name ="userpage"),
path('add_comment/<int:pk>/', views.add_comment,name ="comment"),
    ]