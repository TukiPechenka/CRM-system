from django.urls import path

from .views import (
    AdListView,
    AdsStatisticListView,
    AdCreateView,
    AdDetailView,
    AdUpdateView,
    AdDeleteView,
)


app_name = "advertisements"  # pylint: disable=invalid-name

urlpatterns = [
    path("", AdListView.as_view(), name="ads-list"),
    path("statistic/", AdsStatisticListView.as_view(), name="ads-statistic"),
    path("new/", AdCreateView.as_view(), name="ads-create"),
    path("<int:pk>/", AdDetailView.as_view(), name="ads-detail"),
    path("<int:pk>/edit/", AdUpdateView.as_view(), name="ads-update"),
    path("<int:pk>/delete/", AdDeleteView.as_view(), name="ads-delete"),
]
