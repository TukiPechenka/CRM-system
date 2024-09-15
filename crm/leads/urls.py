from django.urls import path

from .views import (
    LeadListView,
    LeadCreateView,
    LeadDetailView,
    LeadUpdateView,
    LeadDeleteView,
)


app_name = "leads"  # pylint: disable=invalid-name

urlpatterns = [
    path("", LeadListView.as_view(), name="leads-list"),
    path("new/", LeadCreateView.as_view(), name="leads-create"),
    path("<int:pk>/", LeadDetailView.as_view(), name="leads-detail"),
    path("<int:pk>/edit/", LeadUpdateView.as_view(), name="leads-update"),
    path("<int:pk>/delete/", LeadDeleteView.as_view(), name="leads-delete"),
]
