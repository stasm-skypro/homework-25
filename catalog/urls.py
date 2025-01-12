"""
URL configuration for app catalog configuring.
"""

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts_view, product_details_view, ProductListView, add_product_view


app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list.html"),
    # path("", home_view, name="home.html"),
    path("contacts/", contacts_view, name="contacts.html"),
    path("product_details/<int:product_id>", product_details_view, name="product_details.html"),
    path("add_product/", add_product_view, name="add_product.html"),
]
