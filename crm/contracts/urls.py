from django.urls import path

from .views import (
    ContractListView,
    ContractDetailView,
    ContractUpdateView,
    ContractCreateView,
    ContractDeleteView,
)

app_name = "contracts"  # pylint: disable=invalid-name

urlpatterns = [
    path("", ContractListView.as_view(), name="contracts-list"),
    path("new/", ContractCreateView.as_view(), name="contracts-create"),
    path("<int:pk>/", ContractDetailView.as_view(), name="contracts-detail"),
    path(
        "<int:pk>/edit/",
        ContractUpdateView.as_view(),
        name="contracts-update",
    ),
    path(
        "<int:pk>/delete/",
        ContractDeleteView.as_view(),
        name="contracts-delete",
    ),
]
