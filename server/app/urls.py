from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.blog, name="blog"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),

    
    path("events/", views.events, name="events"),
    path("blog_category_1/", views.blog_category_1, name="blog_category_1"),
    path("blog_category_2/", views.blog_category_2, name="blog_category_2"),
    path("", views.index, name='index'),
]

