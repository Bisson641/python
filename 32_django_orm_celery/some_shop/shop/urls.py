from django.urls import path
from .views import shop_index, categories_with_products_tree, products_view, orders_view

app_name = "shop"
urlpatterns = [
    path("", shop_index, name="shop"),
    path("products/", products_view, name="products"),
    path("orders/", orders_view, name="orders"),
    path("categories-tree/", categories_with_products_tree, name="categories_with_products_tree")
]
