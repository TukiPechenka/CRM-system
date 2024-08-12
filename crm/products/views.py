from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Product


class ProductListView(ListView):
    """
    Представление для краткого обзора Продуктов.
    """

    model = Product
    template_name = "products/products-list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    """
    Представление для просмотра деталей Продукта.
    """

    model = Product
    template_name = "products/products-detail.html"


class ProductCreateView(CreateView):
    """
    Представление для создания Продукта.
    """

    model = Product
    fields = "name", "description", "cost"
    template_name = "products/products-create.html"

    def get_success_url(self):
        return reverse("products:products-detail", kwargs={"pk": self.object.pk})


class ProductUpdateView(UpdateView):
    """
    Представление для обновления/редактирования Продукта.
    """

    model = Product
    fields = "name", "description", "cost"
    template_name = "products/products-edit.html"

    def get_success_url(self):
        return reverse("products:products-detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    """
    Представление для страницы удаления Продукта.
    """

    model = Product
    template_name = "products/products-delete.html"
    success_url = reverse_lazy("products:products-list")
