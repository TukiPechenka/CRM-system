from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Представление Услуги в административном интерфейсе
    """

    list_display = "pk", "name", "description", "cost"
