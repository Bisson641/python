from django.db.models import Q
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Product
from .models import Category
from .models import Order

# Create your views here.


def shop_index(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="shop/index.html", context={},)


def products_view(request: HttpRequest) -> HttpResponse:
    products = (Product.objects
                .filter(~Q(status=Product.Status.ARCHIVED))
                .order_by("id")
                .defer(
                    "description",
                    "created_at",
                    "updated_at",
                    "category__description",
                )
                .select_related("category").all())
    return render(request=request, template_name="shop/products.html", context={"products": products},)


def orders_view(request: HttpRequest) -> HttpResponse:
    orders = (Order
              .objects
              .select_related("user", "payment_details")
              .prefetch_related("products")
              .order_by("id")
              .all())
    return render(
        request=request,
        template_name='shop/orders.html',
        context={
            "orders": orders
        }
    )


def categories_with_products_tree(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.order_by("id").prefetch_related("products").all()
    return render(
        request=request,
        template_name="shop/categories_with_products_tree.html",
        context={
            "categories": categories
        }
    )
