from django.db import models
from django.contrib.auth.models import User
from userPage.models import Profile
class Posts(models.Model):
    choices = (('tech','tech'),('news','news'),('health','health')
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    # date_posted = models.DateField()
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
    

