from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("auth/", include("modules.auth.routes")),

    path("tweets/", include("modules.tweets.routes")),
    path("<str:username>/", include("modules.users.routes")),
]
