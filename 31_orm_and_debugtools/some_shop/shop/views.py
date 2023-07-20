from django.db.models import Q
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Product
from .models import Category

# Create your views here.


def shop_index(request: HttpRequest) -> HttpResponse:
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
    return render(request=request, template_name="shop/index.html", context={"products": products},)


def categories_with_products_tree(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.order_by("id").prefetch_related("products").all()
    return render(
        request=request,
        template_name="shop/categories_with_products_tree.html",
        context={
            "categories": categories
        }
    )
