from django.urls import path
from django.contrib.auth.views import LoginView

from .views import (
    IndexTemplateView,
    LogoutView,
)


app_name = "crmsystem"

urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path(
        "login/",
        LoginView.as_view(
            template_name="registration/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
