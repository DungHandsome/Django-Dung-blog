from django.contrib import admin
from .models import blogCategory, blogPost, usersetup
# Register your models here.
admin.site.register(blogCategory)
admin.site.register(blogPost)
admin.site.register(usersetup)