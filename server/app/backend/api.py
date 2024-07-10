from django.urls import path

from . import methods
    

urlpatterns = [
    path("dog_picture/", methods.dog_picture, name="dog_picture"),
    path('random_user/', methods.random_user, name='random_user'),
    path('blog_create/', methods.blog_create, name='blog_create'),
    path('blog_delete/<int:pk>/', methods.blog_delete, name='blog_delete'),
]