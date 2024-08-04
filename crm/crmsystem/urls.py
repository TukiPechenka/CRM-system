from django.urls import path
from django.contrib.auth.views import LoginView

from .views import (
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    ProductDeleteView,
    ProductUpdateView,

    AdListView,
    AdCreateView,
    AdDetailView,
    AdDeleteView,
    AdUpdateView,
    AdsStatisticListView,
)


app_name = "crmsystem"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="registration/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("products/", ProductListView.as_view(), name="products-list"),
    path("products/new/", ProductCreateView.as_view(), name="products-create"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products-detail"),
    path(
        "products/<int:pk>/edit/", ProductUpdateView.as_view(), name="products-update"
    ),
    path(
        "products/<int:pk>/delete/", ProductDeleteView.as_view(), name="products-delete"
    ),

    path('ads/', AdListView.as_view(), name='ads-list'),
    path('ads/statistic/', AdsStatisticListView.as_view(), name='ads-statistic'),
    path('ads/new/', AdCreateView.as_view(), name='ads-create'),
    path('ads/<int:pk>/', AdDetailView.as_view(), name='ads-detail'),
    path('ads/<int:pk>/edit/', AdUpdateView.as_view(), name='ads-update'),
    path('ads/<int:pk>/delete/', AdDeleteView.as_view(), name='ads-delete'),
]
