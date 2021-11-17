from django.urls import path

from modules.users.index import (
    user_info,
    user_tweets,
    user_medias,
    user_replies,
    user_likes,
)

urlpatterns = [
    path("", user_info, name="info"),
    path("tweets", user_tweets, name="tweets"),
    path("medias", user_medias, name="medias"),
    path("likes", user_likes, name="likes"),
    path("comments", user_replies, name="comments"),
]
