from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hello_world", views.hello_world, name="hello_world"),
    path("dog_picture", views.dog_picture, name="dog_picture"),
    path('random_user/', views.random_user, name='random_user'),
    path('pie_chart/', views.pie_chart, name='pie_chart'),
]
