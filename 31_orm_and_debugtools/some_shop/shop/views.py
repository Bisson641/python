from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Product

# Create your views here.

def shop_index(request: HttpRequest) -> HttpResponse:
    products = Product.objects.order_by("id").all()
    return render(request=request, template_name="shop/index.html", context={"products": products},)
