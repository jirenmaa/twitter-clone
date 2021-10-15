from django.http import JsonResponse

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken

from modules.v1.tweets.serializers import (
    TweetSerializer,
    TweetDetailCommentSerializer,
    TweetResponseLikeSerializer,
)

from .models import User


class BaseUserApiView(GenericAPIView):
    """User Base API view"""

    permission_classes = (IsAuthenticated,)

    def get_token(self):
        # get bearer token from request
        tokens = self.request.META.get("HTTP_AUTHORIZATION", " ").split()[-1]
        # get access token from bearer token
        access = AccessToken(tokens)
        return access


class UserTweetsApiView(BaseUserApiView):
    """Retrive all user created tweets"""

    def get(self, request, *args, **kwargs):
        try:
            # get user id from access token
            user_id = self.get_token().payload.get("user_id")
            # get all tweets from user
            user_tweets = (
                User.objects.get(id=user_id).tweets.all().order_by("-created_at")
            )
            queryset = self.filter_queryset(user_tweets)
            serializer = TweetSerializer(
                queryset, many=True, context={"request": request}
            )

            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


index = UserTweetsApiView.as_view()


class UserResponseCommentApiView(BaseUserApiView):
    """Retrive all user created comments"""

    def get(self, request, *args, **kwargs):
        try:
            # get user id from access token
            user_id = self.get_token().payload.get("user_id")
            # get all comments from user
            user_comments = User.objects.get(id=user_id).commented_tweets.all()
            queryset = self.filter_queryset(user_comments)
            # serialize commented tweets
            serializer = TweetDetailCommentSerializer(
                queryset, many=True, context={"request": request}
            )

            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


user_comments = UserResponseCommentApiView.as_view()


class UserResponseLikeApiView(BaseUserApiView):
    """Retrive all user liked tweets"""

    def get(self, request, *args, **kwargs):
        try:
            # get user id from access token
            user_id = self.get_token().payload.get("user_id")
            # get all likes from user
            user_likes = User.objects.get(id=user_id).liked_tweets.all()
            queryset = self.filter_queryset(user_likes)
            # serialize user likes tweets
            serializer = TweetResponseLikeSerializer(
                queryset, many=True, context={"request": request}
            )

            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


user_likes = UserResponseLikeApiView.as_view()
