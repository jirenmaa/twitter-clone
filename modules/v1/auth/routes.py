from django.urls import path

from . import index as views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("activate/", views.activate, name="activate"),
    path("reset_activation/", views.reset_activation, name="reset_activation"),

    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
