from django.urls import path

from modules.tweets.index import (
    tweet_public,
    tweet_detail,
    tweet_responses,
    tweet_responses_like,
    tweet_responses_reply,
)

urlpatterns = [
    path("", tweet_public, name="tweets"),
    path("<str:id>", tweet_detail, name="detail"),
    path("replies/<str:id>", tweet_responses, name="detail_replies"),
    path("like/<str:id>", tweet_responses_like, name="response_like"),
    path("comment/", tweet_responses_reply, name="response_comment"),
]
