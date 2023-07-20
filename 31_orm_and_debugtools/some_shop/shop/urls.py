from django.urls import path
from .views import shop_index, categories_with_products_tree

app_name = "shop"
urlpatterns = [
    path("", shop_index, name="shop"),
    path("categories-tree/", categories_with_products_tree, name="categories_with_products_tree")
]
