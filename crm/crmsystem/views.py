from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View
from django.views.generic import (
    TemplateView,
)

from advertisements.models import Advertisement
from customers.models import Customer
from leads.models import Lead
from products.models import Product


class IndexTemplateView(TemplateView):
    """
    Представление главной страницы приложения
    """

    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products_count"] = Product.objects.count()  # pylint: disable=no-member
        context["advertisements_count"] = (
            Advertisement.objects.count()  # pylint: disable=no-member
        )
        context["leads_count"] = Lead.objects.filter(  # pylint: disable=no-member
            is_customer=False
        ).count()
        context["customers_count"] = (
            Customer.objects.count()  # pylint: disable=no-member
        )
        return context


class LogoutView(View):
    """
    Представление выхода пользователя из аккаунта
    """

    def get(self, request: HttpRequest):
        """
        Метод выхода из аккаунта пользователя
        """
        logout(request)
        return redirect("crmsystem:login")
