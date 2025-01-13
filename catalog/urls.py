"""
URL configuration for app catalog configuring.
"""

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, ProductListView, ProductCreateView


app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("product_detail/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("product_form/", ProductCreateView.as_view(), name="product_create"),
]
