from django.shortcuts import render

from blog.models import Blog
from django.views.generic import ListView

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
