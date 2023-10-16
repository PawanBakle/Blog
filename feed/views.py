from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
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
   title = "Gladiator"
   context = {'title' : title,'post' :posts}
   return render(request,'feed/main.html',context)
def about(request):


   return render(request,'feed/page.html')