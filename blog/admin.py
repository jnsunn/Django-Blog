from django.contrib import admin
from .models import Blog, BlogType


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'get_read_num','blog_type', 'create_time', 'last_update_time')