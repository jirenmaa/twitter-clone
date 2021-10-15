from django.urls import path

from . import index as views

urlpatterns = [
    path("", views.index, name="index"),
    path("likes", views.user_likes, name="likes"),
    path("comments", views.user_comments, name="comments"),
]
