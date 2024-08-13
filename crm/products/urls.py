from django.urls import path

from .views import (
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = "products"  # pylint: disable=invalid-name

urlpatterns = [
    path("", ProductListView.as_view(), name="products-list"),
    path("new/", ProductCreateView.as_view(), name="products-create"),
    path("<int:pk>/", ProductDetailView.as_view(), name="products-detail"),
    path("<int:pk>/edit/", ProductUpdateView.as_view(), name="products-update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="products-delete"),
]
