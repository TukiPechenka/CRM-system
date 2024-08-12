from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Advertisement


class AdListView(ListView):
    """
    Представление краткой информации о Рекламных компаниях
    """

    model = Advertisement
    template_name = "ads/ads-list.html"
    context_object_name = "ads"


class AdDetailView(DetailView):
    """
    Представление детальной информации о Рекламной компании
    """

    queryset = Advertisement.objects.select_related("product").all()
    template_name = "ads/ads-detail.html"


class AdCreateView(CreateView):
    """
    Представление создания Рекламной компании
    """

    model = Advertisement
    template_name = "ads/ads-create.html"
    fields = "name", "product", "promotionChannel", "budget"

    def get_success_url(self):
        return reverse("advertisements:ads-detail", kwargs={"pk": self.object.pk})


class AdUpdateView(UpdateView):
    """
    Представление изменения Рекламной компании
    """

    model = Advertisement
    template_name = "ads/ads-edit.html"
    fields = "name", "product", "promotionChannel", "budget"

    def get_success_url(self):
        return reverse("advertisements:ads-detail", kwargs={"pk": self.object.pk})


class AdDeleteView(DeleteView):
    """
    Представление удаления Рекламной компании
    """

    model = Advertisement
    template_name = "ads/ads-delete.html"
    success_url = reverse_lazy("advertisements:ads-list")


class AdsStatisticListView(ListView, PermissionRequiredMixin):
    """
    Представление статистики по всем Рекламным компаниям
    """

    permission_required = "advertisements.view_statistics"
    template_name = "ads/ads-statistic.html"
    model = Advertisement
    context_object_name = "ads"
