from django.db import models
from django.contrib.auth.models import User
from userPage.models import Profile
import uuid
class Posts(models.Model):
    choices = (('tech','tech'),('news','news'),('health','health')
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    tag = models.CharField(max_length=100,choices=choices)
    def __str__(self):
        return self.title
class Comments(models.Model):
    text = models.TextField()
    u_name = models.ForeignKey(User,on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts,on_delete=models.CASCADE)
    def __str__(self):
        return self.text[:20]
    

class UserData(models.Model):
    user_id = models.CharField(max_length=50)
    full_name = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(max_length=20,null=True,blank=True)
    country = models.CharField(max_length=20,null=True,blank=True)
    profile_picture = models.URLField(max_length=100,null=True,blank=True)
    source = models.URLField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f'id - {self.user_id},full name - {self.full_name},email - {self.email},country - {self.country}'
