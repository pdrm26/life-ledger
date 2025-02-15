from django.urls import path

from .views import home_view, login_account, register_account

urlpatterns = [
    path("", home_view, name="home"),
    path("account/register", register_account, name="register"),
    path("account/login", login_account, name="login"),
]
