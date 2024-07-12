from django.contrib import admin
from .models import Blog, Event

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'author')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'date')
