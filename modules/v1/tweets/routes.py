from django.urls import path

from . import index as views

urlpatterns = [
    path("", views.tweets, name="tweets"),
    path("<str:id>", views.detail, name="detail"),
    path("like/<str:id>", views.response_like, name="response_like"),
    path("comment/", views.response_comment, name="response_comment"),
]
