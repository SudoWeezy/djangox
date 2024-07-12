# Cheat Sheet

## Add a new Db object

`server/app/models.py`

create class ex:

```python
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

`server/app/amdin.py`

import class ex:

```python
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'author')
```

`server/app/form.py`

add form

```python
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'content']
```

```console
python manage.py makemigrations
python manage.py migrate
```
