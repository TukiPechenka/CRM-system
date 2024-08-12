from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Customer


class CustomerListView(ListView):
    """
    Представление списка краткой информации о Клиентах
    """

    queryset = Customer.objects.select_related("lead").select_related("contract").all()
    template_name = "customers/customers-list.html"
    context_object_name = "customers"


class CustomerDetailView(DetailView):
    """
    Представление детальной информации о Клиенте
    """

    queryset = Customer.objects.select_related("lead").select_related("contract").all()
    template_name = "customers/customers-detail.html"


class CustomerCreateView(CreateView):
    """
    Представление создания Клиента
    """

    queryset = Customer.objects.select_related("lead").select_related("contract").all()
    template_name = "customers/customers-create.html"
    fields = "lead", "contract"

    def get_success_url(self):
        return reverse("customers:customers-detail", kwargs={"pk": self.object.pk})


class CustomerUpdateView(UpdateView):
    """
    Представление изменения Клиента
    """

    queryset = Customer.objects.select_related("lead").select_related("contract").all()
    template_name = "customers/customers-edit.html"
    fields = "lead", "contract"

    def get_success_url(self):
        return reverse("customers:customers-detail", kwargs={"pk": self.object.pk})


class CustomerDeleteView(DeleteView):
    """
    Представление удаления Клиента
    """

    queryset = Customer.objects.select_related("lead").select_related("contract").all()
    template_name = "customers/customers-delete.html"
    success_url = reverse_lazy("customers:customers-list")
