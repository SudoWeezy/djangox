from django import forms
from .models import Blog, Event
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
class LoginForm(AuthenticationForm):
    pass
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'content']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'author', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'author': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
        }