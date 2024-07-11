from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from .models import Blog



def blog(request):
    # Get the list of tables in the database
    table_names = connection.introspection.table_names()
    # Check if the 'appname_blog' table exists
    if 'app_blog' in table_names:  # Replace 'appname' with your actual app name
        blogs = Blog.objects.all().order_by('-created_at')
        is_empty = not blogs.exists()
    else:
        blogs = []
        is_empty = True

    return render(request, 'main/blog.html', {'blogs': blogs, 'is_empty': is_empty})
def home(request):
   return render(request, 'main/home.html')


def about(request):
   return HttpResponse("about")
def events(request):
   return HttpResponse("events")

def blog_category_1(request):
   return HttpResponse("blog_category_1")
def blog_category_2(request):
   return HttpResponse("blog_category_2")
def index(request):
   return render(request, 'main/index.html')
