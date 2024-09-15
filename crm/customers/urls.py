from django.urls import path

from .views import (
    CustomerListView,
    CustomerCreateView,
    CustomerDetailView,
    CustomerUpdateView,
    CustomerDeleteView,
)

app_name = "customers"  # pylint: disable=invalid-name

urlpatterns = [
    path("", CustomerListView.as_view(), name="customers-list"),
    path("new/", CustomerCreateView.as_view(), name="customers-create"),
    path("<int:pk>/", CustomerDetailView.as_view(), name="customers-detail"),
    path(
        "<int:pk>/edit/",
        CustomerUpdateView.as_view(),
        name="customers-update",
    ),
    path(
        "<int:pk>/delete/",
        CustomerDeleteView.as_view(),
        name="customers-delete",
    ),
]
