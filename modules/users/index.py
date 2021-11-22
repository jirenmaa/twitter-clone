from typing import List

from django.http import JsonResponse

from modules.tweets.models import Tweet, ResponseUserLikedTweet
from modules.tweets.serializers import (
    TweetPublicSerializer,
    UserTweetPublicLikesSerializer,
)
from modules.users.serializers import UserPublicInfoSerializer
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

    def list(self, request, username: str, *args, **kwargs):
        """return list of user tweet with pagination"""
        try:
            # serialize data from database and paginate
            # by default, paginate by 10
            queryset = self.filter_queryset(self.get_queryset(username))
            serializer = self.get_serializer(queryset, many=True)

            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)

    def retrive_token(self, request) -> AccessToken:
        """get token from authorization header"""
        tokens = request.META.get("HTTP_AUTHORIZATION", " ").split()[-1]
        access = AccessToken(tokens)
        return access


class UserPublicInfoVuew(UserBaseApi):
    """view for user public info"""

    serializer_class = UserPublicInfoSerializer

    def get_queryset(self, username: str) -> User:
        """get user querset"""
        return User.objects.get(username=username, is_active=True)

    def get(self, request, username: str, *args, **kwargs):
        """get user public info"""
        try:
            queryset = self.get_queryset(username)
            serializer = self.get_serializer(queryset)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)


class UserPublicTweetView(UserBaseApi):
    """user public tweet api views
    methods: get, delete
    """

    serializer_class = TweetPublicSerializer

    def get_queryset(self, username: str) -> List[Tweet]:
        """return list of user tweet"""
        return (
            User.objects.get(username=username, is_active=True)
            .tweets.all()
            .order_by("-created_at")
        )

    def get(self, request, username: str, *args, **kwargs):
        """return list of user tweeted tweets"""
        return self.list(request, username, *args, **kwargs)


class UserPublicMediaView(UserBaseApi):
    """user public tweet medias api views
    methods: get
    """

    serializer_class = TweetPublicSerializer

    def get_queryset(self, username: str) -> List[Tweet]:
        """return list of user tweet"""
        return (
            User.objects.get(username=username, is_active=True)
            .tweets.all()
            .exclude(pictures="")
            .order_by("-created_at")
        )

    def get(self, request, username: str, *args, **kwargs):
        """return list of user tweeted medias"""
        return self.list(request, username, *args, **kwargs)


class UserPublicReplyView(UserBaseApi):
    """user public tweet replies api views
    methods: get
    """

    serializer_class = TweetPublicSerializer

    def get_queryset(self, username: str) -> List[Tweet]:
        """return list of user tweet"""
        return (
            User.objects.get(username=username, is_active=True)
            .commented_tweets.all()
            .order_by("-created_at")
        )

    def get(self, request, username: str, *args, **kwargs):
        """return list of user tweeted replies"""
        return self.list(request, username, *args, **kwargs)


class UserPublicLikesView(UserBaseApi):
    """user public tweet likes api views
    methods: get
    """

    serializer_class = UserTweetPublicLikesSerializer

    def list(self, request, username: str, *args, **kwargs):
        """return list of user tweet with pagination"""
        try:
            # serialize data from database and paginate
            # by default, paginate by 10
            queryset = self.filter_queryset(self.get_queryset(username))
            serializer = self.get_serializer(
                queryset, many=True, context={"request": request}
            )

            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self, username: str) -> List[ResponseUserLikedTweet]:
        """return list of user tweet"""
        return (
            User.objects.get(username=username, is_active=True)
            .liked_tweet.all()
            .order_by("-created_at")
        )

    def get(self, request, username: str, *args, **kwargs):
        """return list of user tweeted replies"""
        return self.list(request, username, *args, **kwargs)


user_info = UserPublicInfoVuew.as_view()
user_tweets = UserPublicTweetView.as_view()
user_medias = UserPublicMediaView.as_view()
user_replies = UserPublicReplyView.as_view()
user_likes = UserPublicLikesView.as_view()
