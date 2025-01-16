# blog/views.py
import logging

from django.urls import reverse_lazy

from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView


logger = logging.getLogger("blog")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("blog/logs/reports.log", "a", "utf-8")
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s"))
logger.addHandler(handler)

class BlogListView(ListView):
    """
    Определяет отображение страницы блога.
    """
    model = Blog
    context_object_name = 'blog_list'


class BlogDetailView(DetailView):
    """
    Определяет отображение страницы с содержимым статьи.
    """
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1

        # Отправлять уведомление администратору, если количество просмотров превысило 100
        if self.object.views_counter >= 100:
            logger.info("Количество просмотров превысило %s." % self.object.views_counter)
        self.object.save()

        return self.object


class BlogCreateView(CreateView):
    """
    Определяет отображение страницы добавления статьи.
    """
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        """
        Дополнительная обработка перед сохранением формы.
        """
        self.object = form.save()  # Сохраняем объект формы в базу
        logger.info("Продукт '%s' успешно создан." % self.object.product)
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Обработка в случае неверной формы.
        """
        logger.warning("Ошибка при создании продукта: %s" % form.errors)
        return super().form_invalid(form)
