from django.urls import path
from django.views.generic import TemplateView
from .views import LoginView, LogoutView, RegisterView

app_name = "site_auth"
urlpatterns = [
    # path("login/", TemplateView.as_view(template_name='site_auth/login.html'), name="login",),
    path("login/", LoginView.as_view(), name="login",),
    path("logout/", LogoutView.as_view(), name="logout",),
    path("register/", RegisterView.as_view(), name="register",),
    path("me/", TemplateView.as_view(template_name="site_auth/me.html"), name="about-me"),
]
