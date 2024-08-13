from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Contract


class ContractListView(ListView):
    """
    Представление краткой информации о Контрактах
    """

    queryset = Contract.objects.select_related(  # pylint: disable=no-member
        "product"
    ).all()
    template_name = "contracts/contracts-list.html"
    context_object_name = "contracts"


class ContractDetailView(DetailView):
    """
    Представление детальной информации о Контракте
    """

    queryset = Contract.objects.select_related(  # pylint: disable=no-member
        "product"
    ).all()
    template_name = "contracts/contracts-detail.html"


class ContractCreateView(CreateView):
    """
    Представление создания Контракта
    """

    queryset = Contract.objects.select_related(  # pylint: disable=no-member
        "product"
    ).all()
    template_name = "contracts/contracts-create.html"
    fields = "name", "product", "document", "start_date", "end_date", "cost"

    def get_success_url(self):
        return reverse("contracts:contracts-detail", kwargs={"pk": self.object.pk})


class ContractUpdateView(UpdateView):
    """
    Представление обновления Контракта
    """

    queryset = Contract.objects.select_related(  # pylint: disable=no-member
        "product"
    ).all()
    template_name = "contracts/contracts-edit.html"
    fields = "name", "product", "document", "start_date", "end_date", "cost"

    def get_success_url(self):
        return reverse("contracts:contracts-detail", kwargs={"pk": self.object.pk})


class ContractDeleteView(DeleteView):
    """
    Представление удаления Контракта
    """

    queryset = Contract.objects.select_related(  # pylint: disable=no-member
        "product"
    ).all()
    template_name = "contracts/contracts-delete.html"
    success_url = reverse_lazy("contracts:contracts-list")
