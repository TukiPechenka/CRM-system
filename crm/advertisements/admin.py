from django.contrib import admin

from .models import Advertisement


@admin.register(Advertisement)
class AdAdmin(admin.ModelAdmin):
    """
    Интерфейс административной панели для работы с моделями Рекламных Компаний.
    """

    list_display = (
        "pk",
        "name",
        "product",
        "promotionChannel",
        "budget",
        "profit",
        "leads_count",
        "customers_count",
    )
    readonly_fields = "profit", "leads_count", "customers_count"
