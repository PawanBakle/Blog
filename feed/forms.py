from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Posts,Comments
from django.forms import ModelForm
class NewPost(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'tag']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'tag': forms.Select(attrs={'class': 'form-select'}),
        }

class Post_edit(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title','content')
class Comment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
