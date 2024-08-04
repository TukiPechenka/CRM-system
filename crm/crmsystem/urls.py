from django.urls import path
from django.contrib.auth.views import LoginView


app_name = 'crmsystem'

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='registration/login.html', redirect_authenticated_user=True,
    ))
]