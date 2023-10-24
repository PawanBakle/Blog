from django.db import models
from django.contrib.auth.admin import User
class Posts(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    # date_posted = models.DateField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='postss')
    def __str__(self):
        return self.title
