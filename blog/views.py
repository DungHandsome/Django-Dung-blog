from django.shortcuts import render
from .models import blogPost, blogCategory
# Create your views here.
def home(request):
    data = {
        'Posts': blogPost.objects.all().order_by('-date'),
        'Categories': blogCategory.objects.all().order_by('-categoryname'),
    }
    return render(request, 'blog/home.html', data)

def blog_post(request, id):
    post = blogPost.objects.get(id=id)
    return render(request, 'blog/blog_post.html', {'post': post})