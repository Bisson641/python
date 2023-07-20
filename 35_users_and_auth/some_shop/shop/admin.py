from django.contrib import admin

from .models import Product
from .models import Category
from .models import Order
from .models import OrderPaymantDetails



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description", "updated_at"
    list_display_links = "id", "name"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description", "archived"
    list_display_links = "id", "name"

class PaymentDetailsInLine(admin.TabularInline):
    model = OrderPaymantDetails



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        PaymentDetailsInLine,
    ]
    list_display = "id", "user", "address", "promocode", "created_at"
    list_display_links = "id", "promocode"
    # fields = (
    #     "id",
    #     "user",
    #     "address",
    #     "promocode",
    #     "created_at",
    #     "payment_details",
    # )


@admin.register(OrderPaymantDetails)
class OrderPaymentDetailsAdmin(admin.ModelAdmin):
    list_display = "id", "payed_at", "card_end_with", "status", "order"
    list_display_links = "id", "status"
