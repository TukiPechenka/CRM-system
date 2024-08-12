from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """
    Представление Контракта в административном интерфейсе
    """

    list_display = "pk", "name", "product", "document", "start_date", "end_date", "cost"
