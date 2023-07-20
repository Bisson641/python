from http import HTTPStatus

from django.db.models import Q
from django.test import TestCase
from django.urls import reverse

from shop.models import Product


class ProductsListTestCase(TestCase):
    fixtures = [
        "category-fixtures.json",
        "product-fixtures.json"
    ]

    def test_ok(self):
        products_qs = (Product.objects
                       .filter(~Q(status=Product.Status.ARCHIVED))
                       .order_by("id")
                       .defer(
                        "description",
                        "created_at",
                        "updated_at",
                        "category__description",
                        )
                       .select_related("category")
                       .all())
        url = reverse("shop:products")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "shop/products.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertQuerySetEqual(qs=products_qs,
                                 values=(p.pk for p in response.context["products"]),
                                 transform=lambda p: p.pk,
                                 )
