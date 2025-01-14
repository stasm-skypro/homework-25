"""
Контроллеры, определённые внутри приложения catalog.
"""

from django.urls import reverse_lazy
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    """
    Определяет отображение страницы product_list.html.
    """

    model = Product
    # По правилам CBV имя шаблона нужно задать как <app_name>/<model_name>_<action>. Тогда можно было бы обойтись
    # без переменных template_name и context_object_name. Для реализации такого подхода нужно создать в папке
    # templates подкаталог catalog, переместить все шаблоны в этот подкаталог и скорректировать пути внутри шаблонов.

    # template_name = "product_list.html"
    context_object_name = "product_list"


class ProductDetailView(DetailView):
    """
    Определяет отображение детализации (характеристик) продукта.
    """

    model = Product
    # template_name = "product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    """
    Определяет отображение добавления продукта.
    """

    model = Product
    fields = ["product", "description", "image", "category", "price", "created_at", "changed_at"]
    # template_name = "product_form"
    # context_object_name = "product_create"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        """
        Дополнительная обработка перед сохранением формы.
        """
        self.object = form.save()  # Сохраняем объект формы в базу
        print("Форма прошла валидацию")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Обработка в случае неверной формы.
        """
        print("Форма не прошла валидацию")
        print(form.errors)  # Вывод ошибок формы в консоль
        return super().form_invalid(form)


class ProductUpdateView(UpdateView):
    """
    Определяет отображение обновления продукта.
    """

    model = Product
    fields = ["product", "description", "image", "category", "price", "created_at", "changed_at"]
    # template_name = "product_form"
    # context_object_name = "product_update"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        """
        Дополнительная обработка перед сохранением формы.
        """
        self.object = form.save()  # Сохраняем объект формы в базу
        print("Форма прошла валидацию")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Обработка в случае неверной формы.
        """
        print("Форма не прошла валидацию")
        print(form.errors)  # Вывод ошибок формы в консоль
        return super().form_invalid(form)


class ProductDeleteView(DeleteView):
    """
    Определяет отображение удаления продукта.
    """

    model = Product
    fields = ["product", "description", "image", "category", "price", "created_at", "changed_at"]
    # template_name = "product_delete"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:product_list")  # Перенаправление на страницу product_list
