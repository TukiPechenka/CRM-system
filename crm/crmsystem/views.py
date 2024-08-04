from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Product, Ad, Lead, Contract, Customer


class ProductListView(ListView):
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/products-detail.html'


class ProductCreateView(CreateView):
    model = Product
    fields = 'name', 'description', 'cost'
    template_name = 'products/products-create.html'

    def get_success_url(self):
        return reverse('crm:products-detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    fields = 'name', 'description', 'cost'
    template_name = 'products/products-edit.html'

    def get_success_url(self):
        return reverse('crm:products-detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('crm:products-list')


