from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class HelloViewTestCase(TestCase):
    def test_get_ok(self):
        url = reverse("shop:hello")
        response = self.client.get(url)
        self.assertHTMLEqual(response.content.decode(), "<h1>Hello View</h1>")


class ShopIndexView(TestCase):

    def test_index_view_status_ok(self):
        url = reverse('shop:shop')
        response = self.client.get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)
        # self.assertInHTML( "<h1>Shop index</h1>", response.body, count=1)
