from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("account/register", views.register_account, name="register"),
    path("account/login", views.login_account, name="login"),
]
