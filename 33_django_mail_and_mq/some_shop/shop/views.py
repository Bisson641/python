from celery.result import AsyncResult
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Product
from .models import Category
from .models import Order
from .tasks import notify_order_saved

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


def get_task_info(request: HttpRequest, task_id: str) -> HttpResponse:
    task_result : AsyncResult = notify_order_saved.AsyncResult(task_id)
    return JsonResponse({
        "task_id": task_result.id,
        "status": task_result.status,
        "name": task_result.name,
        # "backend": str(task_result.backend),
    })
