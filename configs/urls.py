from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("auth/", include("modules.auth.routes")),

    path("tweets/", include("modules.tweets.routes")),
    path("user/", include("modules.users.routes")),
]
