from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description", "updated_at"
    list_display_links = "id", "name"
