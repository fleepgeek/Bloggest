from django.contrib import admin
from .models import Post, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)