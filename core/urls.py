from django.urls import path
from .views import home_view, register_account, login_account


urlpatterns = [
    path("", home_view, name="home"),
    path("account/register", register_account, name="register_account"),
    path("account/login", login_account, name="login_account"),
]
