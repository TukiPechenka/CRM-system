from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    """
    Представление Потенциального Клиента в административном интерфейсе
    """

    list_display = (
        "pk",
        "first_name",
        "last_name",
        "phone",
        "email",
        "ad",
        "is_customer",
    )
