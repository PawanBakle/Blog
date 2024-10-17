from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Posts,Comments
from django.forms import ModelForm
class NewPost(forms.ModelForm):
    class Meta:
        model=Posts
        author = User.username
        fields= ['title','content']

class Post_edit(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title','content')
class Comment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
