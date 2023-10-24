from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,forms
from .models import Posts
class NewPost(forms.ModelForm):
    class Meta:
        model=Posts
        author = User.username
        fields= ['title','content']
