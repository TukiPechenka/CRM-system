from django.urls import path
from django.contrib.auth.views import LoginView

from .views import ProductListView, ProductCreateView, ProductDetailView, ProductDeleteView, ProductUpdateView


app_name = 'crmsystem'

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='registration/login.html', redirect_authenticated_user=True,
    ), name='login'),
    path('products/', ProductListView.as_view(), name='products-list'),
    path('products/new/', ProductCreateView.as_view(), name='products-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products-detail'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='products-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='products-delete'),
]