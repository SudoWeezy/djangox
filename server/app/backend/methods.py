from django.template.loader import render_to_string
from .decorators import htmx_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import requests
import logging
from ..forms import BlogForm
from ..models import Blog

logger = logging.getLogger(__name__)

@htmx_required
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
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return render(request, 'partials/blog_post.html', {'blog': blog})  # Render partial template with the new blog post

    else:
        form = BlogForm()
    
    if request.method == 'GET':
        return render(request, 'partials/blog_create_form.html', {'form': form})
    
    return HttpResponse("blog_create", status=404)

@htmx_required
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    print("request == " + request.method)
    if request.method == 'DELETE':
        blog.delete()
        return HttpResponse(status=204)
    if request.method == 'GET':
        return render(request, 'partials/blog_delete_confirm.html', {'blog': blog})

    return HttpResponse("blog_delete", status=404)
