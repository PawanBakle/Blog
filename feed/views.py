from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Posts
from .forms import NewPost
from django.contrib.auth.admin import User

posts = [
   {
      'author':'Delulu,',
      'title':'Postday',
      'date':'28-12-2022',
      'content':"A day in a life of "
   },
   {
      'author': 'Lalalla,',
      'title': 'Moderism',
      'date': '09-7-2021',
      'content': "A film based on Art "
   }
]
def home(request):
   posts = Posts.objects.all()
   context = {'post' :posts}
   return render(request,'feed/main.html',context)
def about(request):


   return render(request,'feed/page.html')


def new_posts(request,pk):

   if request.method == 'POST':

      post_form  = NewPost(request.POST)
      if post_form.is_valid():
         post_form.save()
         return redirect('/')
   else:
      post_form = NewPost(request.POST, instance=request.user)

   context = {'post_form':post_form}
   return render(request,'feed/add_post.html',context)