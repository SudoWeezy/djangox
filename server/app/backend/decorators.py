from functools import wraps
from django.shortcuts import render

def htmx_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.headers.get('Hx-Request'):
            return render(request, 'main/404.html')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

