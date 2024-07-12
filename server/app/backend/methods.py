from django.template.loader import render_to_string
from django.http import HttpResponse
from django_htmx.http import HttpResponseClientRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
import requests
import logging
from ..forms import BlogForm, RegisterForm, EventForm
from ..models import Blog, Event
from .decorators import htmx_required, url_pattern

logger = logging.getLogger(__name__)

@htmx_required
@url_pattern('events/new')
def events_new(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseClientRedirect("/events")
    else:
        form = EventForm()
    return render(request, 'partials/event/form.html', {'form': form})

@htmx_required
@url_pattern('event/delete/<int:pk>')
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'DELETE':
        event.delete()
        events = Event.objects.all().order_by('-created_at')
        return render(request, 'partials/event/table.html', {'events': events})
        # return HttpResponseClientRedirect("/events")

    return HttpResponse("event_delete", status=404)


@csrf_exempt
@htmx_required
@url_pattern('event/update/<int:pk>')
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        new_title = request.POST.get('title', None)
        print(new_title)
        if new_title:
            event.title = new_title
            event.save()
            events = Event.objects.all().order_by('-created_at')
            return render(request, 'partials/event/table.html', {'events': events})
        else:
            return HttpResponse("Title not provided", status=400)
    return HttpResponse("Method not allowed", status=405)

@htmx_required
@url_pattern('items/')
def items(request):
    return HttpResponse("Registration successful")

@htmx_required
@url_pattern('register/')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse("Registration successful")
    else:
        form = RegisterForm()
    return render(request, 'partials/auth/register.html', {'form': form})


@htmx_required
@url_pattern('user_login/')
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next', 'home')
            return redirect(next_url)
    else:
        next_url = request.GET.get('next', '/')
        form = AuthenticationForm()
    return render(request, 'partials/auth/login.html', {'form': form, 'next': next_url})

@htmx_required
@url_pattern('user_logout/')
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        next_url = request.POST.get('next', 'home')
        print(next_url)
        return redirect(next_url)

@htmx_required
@url_pattern('login_options/')
def login_options(request):
    if request.method == 'GET':
        next_url = request.GET.get('next')
        print(next_url)
        return render(request, 'partials/auth/login_options.html', {'next': next_url})
    return HttpResponse("login_options", status=404)


@htmx_required
@url_pattern('dog_picture/')
def dog_picture(request):
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        data = response.json()
        image_url = data['message']
        html = render_to_string('partials/dog_image.html', {'image_url': image_url})
        return HttpResponse(html)
    except requests.RequestException as e:
        logger.error(f"Error fetching dog image: {e}")
        return HttpResponse("Failed to fetch dog image", status=500)

@htmx_required
@url_pattern('random_user/')
def random_user(request):
    try:
        response = requests.get('https://randomuser.me/api/')
        response.raise_for_status()
        data = response.json()
        user = data['results'][0]
        html = render_to_string('partials/user.html', {'user': user})
        return HttpResponse(html)
    except requests.RequestException as e:
        logger.error(f"Error fetching user data: {e}")
        return HttpResponse("Failed to fetch user data", status=500)
    
@htmx_required
@url_pattern('blog_create/')
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return render(request, 'partials/blog/post.html', {'blog': blog})  # Render partial template with the new blog post
    else:
        form = BlogForm()
    if request.method == 'GET':
        return render(request, 'partials/blog/create_form.html', {'form': form})
    return HttpResponse("blog_create", status=404)

@htmx_required
@url_pattern('blog_delete/<int:pk>/')
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    print("request == " + request.method)
    if request.method == 'DELETE':
        blog.delete()
        return HttpResponse(status=204)
    if request.method == 'GET':
        return render(request, 'partials/blog/delete_confirm.html', {'blog': blog})

    return HttpResponse("blog_delete", status=404)
