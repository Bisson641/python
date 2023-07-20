from django.contrib import admin

from .models import Product
from .models import Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description", "updated_at"
    list_display_links = "id", "name"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description"
    list_display_links = "id", "name"
