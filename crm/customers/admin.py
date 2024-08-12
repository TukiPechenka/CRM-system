from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Представление клиента в административном интерфейсе
    """

    list_display = "pk", "lead", "contract"
