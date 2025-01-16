# blog urls.py

from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView

app_name = 'blog'

urlpatterns = [
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/create", BlogCreateView.as_view(), name="blog_create"),
]
