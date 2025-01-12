"""
Контроллеры, определённые внутри приложения catalog.
"""

from django.shortcuts import render
from catalog.models import Product
from catalog.forms import ContactForm, ProductForm
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    """
    Определяет отображение страницы home - product_list.html.
    """
    model = Product
    # По правилам CBV имя шаблона нужно задать как catalog/product_list. Тогда можно было бы обойтись без переменных
    # template_name и context_object_name. Для реализации такого подхода нужно создать в папке templates подкаталог
    # catalog, переместить все шаблоны в этот подкаталог и скорректировать пути внутри шаблонов.
    template_name = "product_list.html"
    context_object_name = "home"


class ProductDetailView(DetailView):
    """
    Определяет отображение детализации (характеристик) продукта.
    """
    model = Product
    template_name = "product_details.html"
    context_object_name = "product_details"

# def home_view(request):
#     """
#     Определяет отображение страницы home.html.
#     """
#     products_list = Product.objects.all().order_by("id")
#     return render(request, "catalog/home.html", context={"products_list": products_list})


# def product_details_view(request, product_id: int = 1):
#     """
#     Определяет отображение детализации (характеристик) продукта.
#     """
#     product = Product.objects.get(id=product_id)
#     return render(request, "product_details.html", context={"product": product})


def contacts_view(request):
    """
    Определяет отображение страницы contacts.html.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в таблицу catalog_contacts
            return render(request, "success.html")
    else:
        form = ContactForm()
    return render(request, "contacts.html", {"form": form})


def add_product_view(request):
    """
    Определяет отображение добавления продукта.
    """
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Сохраняем данные в таблицу catalog_products
            return render(request, "success.html")
    else:
        form = ProductForm()
    return render(request, "add_product.html", {"form": form})
