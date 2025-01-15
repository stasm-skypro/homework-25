# blog/views.py

from blog.models import Blog
from django.views.generic import ListView, DetailView


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blog_list'


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog_detail'
