from django.shortcuts import render

from blog.models import Blog
from django.views.generic import ListView

class BlogListView(ListView):
    model = Blog
    context_object_name = 'blog_list'
