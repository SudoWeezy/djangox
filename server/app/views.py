from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from .models import Blog, Event
from .forms import EventForm




def blog(request):
    # Get the list of tables in the database
    table_names = connection.introspection.table_names()
    # Check if the 'appname_blog' table exists
    if 'app_blog' in table_names: 
        blogs = Blog.objects.all().order_by('-created_at')
        is_empty = not blogs.exists()
    else:
        blogs = []
        is_empty = True
    return render(request, 'main/blog.html', {'blogs': blogs, 'is_empty': is_empty})

def home(request):
   return render(request, 'main/home.html')

def about(request):
   projects=["Features", "Marketplace", "Company"]
   roles=["Open roles", "Internship program", "Our values", "Meet our leadership"]
   infos=[
      {"title": "Offices worldwide", "description": "12"},
      {"title": "Full-time colleagues", "description": "300+"},
      {"title": "Hours per week", "description": "40"},
      {"title": "Paid time off", "description": "Unlimited"},
   ]
   products=[
      {
         "icon": '<path stroke-linecap="round" stroke-linejoin="round" d="M10.5 6a7.5 7.5 0 107.5 7.5h-7.5V6z" /> <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 10.5H21A7.5 7.5 0 0013.5 3v7.5z" />',
         "title":"Analytics",
         "description":"Get a better understanding of your traffic"
      },
      {
         "icon": '<path stroke-linecap="round" stroke-linejoin="round" d="M15.042 21.672L13.684 16.6m0 0l-2.51 2.225.569-9.47 5.227 7.917-3.286-.672zM12 2.25V4.5m5.834.166l-1.591 1.591M20.25 10.5H18M7.757 14.743l-1.59 1.59M6 10.5H3.75m4.007-4.243l-1.59-1.59" />',
         "title":"Engagement",
         "description":"Speak directly to your customers"
      },
      {
         "icon": '<path stroke-linecap="round" stroke-linejoin="round" d="M7.864 4.243A7.5 7.5 0 0119.5 10.5c0 2.92-.556 5.709-1.568 8.268M5.742 6.364A7.465 7.465 0 004.5 10.5a7.464 7.464 0 01-1.15 3.993m1.989 3.559A11.209 11.209 0 008.25 10.5a3.75 3.75 0 117.5 0c0 .527-.021 1.049-.064 1.565M12 10.5a14.94 14.94 0 01-3.6 9.75m6.633-4.596a18.666 18.666 0 01-2.485 5.33" />',
         "title":"Security",
         "description":"Your customers’ data will be safe and secure"
      },
      {
         "icon": '<path stroke-linecap="round" stroke-linejoin="round" d="M13.5 16.875h3.375m0 0h3.375m-3.375 0V13.5m0 3.375v3.375M6 10.5h2.25a2.25 2.25 0 002.25-2.25V6a2.25 2.25 0 00-2.25-2.25H6A2.25 2.25 0 003.75 6v2.25A2.25 2.25 0 006 10.5zm0 9.75h2.25A2.25 2.25 0 0010.5 18v-2.25a2.25 2.25 0 00-2.25-2.25H6a2.25 2.25 0 00-2.25 2.25V18A2.25 2.25 0 006 20.25zm9.75-9.75H18a2.25 2.25 0 002.25-2.25V6A2.25 2.25 0 0018 3.75h-2.25A2.25 2.25 0 0013.5 6v2.25a2.25 2.25 0 002.25 2.25z" />',
         "title":"Integrations",
         "description":"Connect with third-party tools"
      },
      {
         "icon": '<path stroke-linecap="round" stroke-linejoin="round" d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99" />',
         "title":"Automations",
         "description":"Build strategic funnels that will convert<"
      },
      {
         "icon": '<path stroke-linecap="round" stroke-linejoin="round" d="M10.5 6a7.5 7.5 0 107.5 7.5h-7.5V6z" /> <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 10.5H21A7.5 7.5 0 0013.5 3v7.5z" />',
         "title":"Analytics",
         "description":"Get a better understanding of your traffic"
      },
   ]
   return render(request, 'pages/about.html', {'projects': projects, "roles": roles, 'infos': infos, 'products': products})


def events(request):
   if request.method == 'GET':
      # Get the list of tables in the database
      table_names = connection.introspection.table_names()
      # Check if the 'appname_blog' table exists
      form = EventForm()
      if 'app_event' in table_names: 
         events = Event.objects.all().order_by('-created_at')
      else:
         events=[]
      return render(request, 'pages/events.html', {'events': events, 'form': form})

def blog_category_1(request):
   return HttpResponse("blog_category_1")
def blog_category_2(request):
   return HttpResponse("blog_category_2")
def index(request):
   return render(request, 'main/index.html')
