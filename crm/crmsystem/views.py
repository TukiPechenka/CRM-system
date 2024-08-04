from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView, TemplateView,
)

from .models import Product, Ad, Lead, Contract, Customer


class ProductListView(ListView):
    model = Product
    template_name = "products/products-list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/products-detail.html"


class ProductCreateView(CreateView):
    model = Product
    fields = "name", "description", "cost"
    template_name = "products/products-create.html"

    def get_success_url(self):
        return reverse("crmsystem:products-detail", kwargs={"pk": self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    fields = "name", "description", "cost"
    template_name = "products/products-edit.html"

    def get_success_url(self):
        return reverse("crmsystem:products-detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/products-delete.html"
    success_url = reverse_lazy("crmsystem:products-list")


class AdListView(ListView):
    model = Ad
    template_name = "ads/ads-list.html"
    context_object_name = "ads"


class AdDetailView(DetailView):
    queryset = Ad.objects.select_related("product")
    template_name = "ads/ads-detail.html"


class AdCreateView(CreateView):
    model = Ad
    template_name = "ads/ads-create.html"
    fields = "name", "product", "promotionChannel", "budget"

    def get_success_url(self):
        return reverse("crmsystem:ads-detail", kwargs={"pk": self.object.pk})


class AdUpdateView(UpdateView):
    model = Ad
    template_name = "ads/ads-edit.html"
    fields = "name", "product", "promotionChannel", "budget"

    def get_success_url(self):
        return reverse("crmsystem:ads-detail", kwargs={"pk": self.object.pk})


class AdDeleteView(DeleteView):
    model = Ad
    template_name = "ads/ads-delete.html"
    success_url = reverse_lazy("crmsystem:ads-list")


class AdsStatisticListView(ListView):
    template_name = 'ads/ads-statistic.html'
    model = Ad
    context_object_name = 'ads'

