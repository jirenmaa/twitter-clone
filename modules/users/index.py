from typing import List

from django.http import JsonResponse

from modules.tweets.models import Tweet
from modules.tweets.serializers import (
    TweetPublicSerializer,
    UserTweetPublicLikesSerializer,
)
from modules.users.models import User

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken


class UserBaseApi(generics.GenericAPIView):
    """base class for user api views"""

    permission_classes = (IsAuthenticated,)
    serializer_class = None

    def get_queryset(self) -> User:
        pass

    def list(self, request, *args, **kwargs):
        """return list of user tweet with pagination"""
        try:
            performer = self.retrive_token(request).payload.get("user_id")
            # serialize data from database and paginate
            # by default, paginate by 10
            queryset = self.filter_queryset(self.get_queryset(performer))
            serializer = self.get_serializer(queryset, many=True)

            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)

    def retrive_token(self, request) -> AccessToken:
        """get token from authorization header"""
        tokens = request.META.get("HTTP_AUTHORIZATION", " ").split()[-1]
        access = AccessToken(tokens)
        return access


class UserPublicTweetView(UserBaseApi):
    """user public tweet api views
    methods: get, delete
    """

    serializer_class = TweetPublicSerializer

    def get_queryset(self, id) -> List[Tweet]:
        """return list of user tweet"""
        return User.objects.get(pk=id).tweets.all().order_by("-created_at")

    def get(self, request, *args, **kwargs):
        """return list of user tweeted tweets"""
        return self.list(request, *args, **kwargs)


class UserPublicMediaView(UserBaseApi):
    """user public tweet medias api views
    methods: get
    """

    serializer_class = TweetPublicSerializer

    def get_queryset(self, id) -> List[Tweet]:
        """return list of user tweet"""
        return (
            User.objects.get(pk=id)
            .tweets.all()
            .exclude(pictures="")
            .order_by("-created_at")
        )

    def get(self, request, *args, **kwargs):
        """return list of user tweeted medias"""
        return self.list(request, *args, **kwargs)


class UserPublicReplyView(UserBaseApi):
    """user public tweet replies api views
    methods: get
    """

    serializer_class = TweetPublicSerializer

    def get_queryset(self, id) -> List[Tweet]:
        """return list of user tweet"""
        return User.objects.get(pk=id).commented_tweets.all()

    def get(self, request, *args, **kwargs):
        """return list of user tweeted replies"""
        return self.list(request, *args, **kwargs)


class UserPublicLikesView(UserBaseApi):
    """user public tweet likes api views
    methods: get
    """

    serializer_class = UserTweetPublicLikesSerializer

    def get_queryset(self, id) -> List[Tweet]:
        """return list of user tweet"""
        return User.objects.get(pk=id).liked_tweet.all().order_by("-created_at")

    def get(self, request, *args, **kwargs):
        """return list of user tweeted replies"""
        return self.list(request, *args, **kwargs)


user_tweets = UserPublicTweetView.as_view()
user_medias = UserPublicMediaView.as_view()
user_replies = UserPublicReplyView.as_view()
user_likes = UserPublicLikesView.as_view()
