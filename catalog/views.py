"""
Контроллеры, определённые внутри приложения catalog.
"""

import logging

from django.urls import reverse_lazy
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


logger = logging.getLogger("catalog")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("catalog/logs/reports.log", "a", "utf-8")
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s"))
logger.addHandler(handler)


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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


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
        # print("Форма прошла валидацию")
        logger.info(f"Продукт '{self.object.product}' успешно создан.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Обработка в случае неверной формы.
        """
        print("Форма не прошла валидацию")
        # print(form.errors)  # Вывод ошибок формы в консоль
        logger.warning(f"Ошибка при создании продукта: {form.errors}")
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
        # print("Форма прошла валидацию")
        logger.info(f"Продукт '{self.object.product}' успешно обновлён.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Обработка в случае неверной формы.
        """
        print("Форма не прошла валидацию")
        # print(form.errors)  # Вывод ошибок формы в консоль
        logger.warning(f"Ошибка при обновлении продукта: {form.errors}")
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

    def post(self, request, *args, **kwargs):
        """
        Переопределение метода POST для вызова delete.
        """
        logger.info(f"Удаление продукта через POST-запрос.")
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Переопределение метода delete для логирования.
        """
        product = self.get_object()
        logger.info(f"Продукт '{product.product}' успешно удалён.")
        return super().delete(request, *args, **kwargs)
