from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.
class usersetup(AbstractUser):
    avatar = models.ImageField(upload_to='user_profile_images', null=True)
class blogCategory(models.Model):
    categoryname = models.CharField(max_length=500)
    categoryicon = models.ImageField(upload_to='category_images', null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.categoryname

class blogPost(models.Model):
    title = models.CharField(max_length=1500)
    sub_title = models.CharField(max_length=5000)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(blogCategory, on_delete=models.CASCADE, null=True)
    coverimage = models.ImageField(upload_to='blog_images', null=True)
    previewicon = models.ImageField(upload_to='preview_images', null=True)
    def __str__(self):
        return self.title
