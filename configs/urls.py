from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("auth/", include("modules.v1.auth.routes")),
    path("user/", include("modules.v1.users.routes")),

    path("tweets/", include("modules.v1.tweets.routes")),
]
