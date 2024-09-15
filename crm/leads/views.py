from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Lead


class LeadListView(ListView):
    """
    Представление списка краткой информации о Потенциальных Клиентов
    """

    queryset = Lead.objects.filter(is_customer=False).all()  # pylint: disable=no-member
    template_name = "leads/leads-list.html"
    context_object_name = "leads"


class LeadDetailView(DetailView):
    """
    Представление детальной информации о Потенциальном Клиенте
    """

    queryset = (
        Lead.objects.filter(is_customer=False)  # pylint: disable=no-member
        .select_related("ad")
        .all()
    )
    template_name = "leads/leads-detail.html"


class LeadCreateView(CreateView):
    """
    Представление создания Потенциального Клиента
    """

    queryset = (
        Lead.objects.filter(is_customer=False)  # pylint: disable=no-member
        .select_related("ad")
        .all()
    )
    template_name = "leads/leads-create.html"
    fields = "first_name", "last_name", "phone", "email", "ad"

    def get_success_url(self):
        return reverse("leads:leads-detail", kwargs={"pk": self.object.pk})


class LeadUpdateView(UpdateView):
    """
    Представление обновления Потенциального Клиента
    """

    queryset = (
        Lead.objects.filter(is_customer=False)  # pylint: disable=no-member
        .select_related("ad")
        .all()
    )
    template_name = "leads/leads-edit.html"
    fields = "first_name", "last_name", "phone", "email", "ad"

    def get_success_url(self):
        return reverse("leads:leads-detail", kwargs={"pk": self.object.pk})


class LeadDeleteView(DeleteView):
    """
    Представление страницы удаления Потенциального клиента
    """

    queryset = (
        Lead.objects.filter(is_customer=False)  # pylint: disable=no-member
        .select_related("ad")
        .all()
    )
    template_name = "leads/leads-delete.html"
    success_url = reverse_lazy("leads:leads-list")
