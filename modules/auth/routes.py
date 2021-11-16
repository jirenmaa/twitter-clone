from django.urls import path

from modules.auth.index import (
    auth_registration,
    auth_activation,
    auth_resetactivation,
    auth_resetpassword,
    auth_login,
    auth_logout,
)

urlpatterns = [
    path("activate/", auth_activation, name="activate"),
    path("reset_activation/", auth_resetactivation, name="reset_activation"),
    path("reset_password/", auth_resetpassword, name="reset_password"),

    path("register/", auth_registration, name="register"),
    path("login/", auth_login, name="login"),
    path("logout/", auth_logout, name="logout"),
]
