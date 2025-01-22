from django.test import TestCase
from django.urls import reverse

from catalog.models import Product, Category


class TestProductListView(TestCase):

    def test_product_list(self):
        response = self.client.get("")
        # print(response.context)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/product_list.html")
        self.assertEqual(response.context["product_list"].count(), Product.objects.all().count())


class TestProductDetailView(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создаем тестовый объект Category
        cls.category = Category.objects.create(
            name="Test Category",
            description="Test Description",
        )

        # Создаем тестовый объект Product
        cls.product = Product.objects.create(
            product="Test Product",
            description="Test Description",
            image = "catalog/milk.png",
            category=Category.objects.get(name="Test Category"),
            price=100.0,
            created_at="2023-01-01",
            changed_at="2023-01-01",
        )

    def test_product_detail(self):
        # Проверяем, что статус-код 200
        url = reverse("catalog:product_detail", kwargs={"pk": self.product.pk})
        print(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_detail_template_used(self):
        # Проверяем, что используется правильный шаблон
        url = reverse("catalog:product_detail", kwargs={"pk": self.product.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "catalog/product_detail.html")

    def test_product_detail_context(self):
        # Проверяем, что объект продукта передается в контекст
        url = reverse("catalog:product_detail", kwargs={"pk": self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.context["product"].product, self.product.product)
        self.assertEqual(response.context["product"].description, self.product.description)
        self.assertEqual(response.context["product"].price, self.product.price)
