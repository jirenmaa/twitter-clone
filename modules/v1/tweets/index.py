from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken

from modules.v1.users.models import User

from .models import Tweet, ResponseComment
from .serializers import (
    TweetSerializer,
    TweetDetailSerializer,
    TweetPostSerializer,
    TweetResponseCommentSerializer,
)


class BaseTweetAPIView(GenericAPIView):
    """Base class for Tweet API views"""

    permission_classes = (IsAuthenticated,)

    def get_token(self):
        # get bearer token from request
        tokens = self.request.META.get("HTTP_AUTHORIZATION", " ").split()[-1]
        # get access token from bearer token
        access = AccessToken(tokens)
        return access


class TweetPublicAPIView(BaseTweetAPIView):
    """
    Tweet Public API views, return list of tweats and recived post tweat from api

    Methods:
        GET, POST

    Authentication:
        Bearer Token
    """

    serializer_class = TweetSerializer

    def get_queryset(self):
        return Tweet.objects.all().order_by("-created_at")

    def list(self, request, *args, **kwargs):
        """Return list of tweats from queryset and serialize them"""
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def get(self, request, *args, **kwargs):
        """Return list of tweats"""
        try:
            return self.list(request)
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        """Create new tweat"""
        try:
            request = request.data.copy()
            # append author data to request to be serialized
            request["author"] = self.get_token().payload.get("user_id")

            serializer = TweetPostSerializer(data=request)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return JsonResponse({}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


tweets = TweetPublicAPIView.as_view()


class TweetDetailAPIView(BaseTweetAPIView):
    """
    Tweet Public API views, return single of tweat

    Methods:
        GET

    Authentication:
        Bearer Token
    """

    serializer_class = TweetDetailSerializer

    def get(self, request, id: str, *args, **kwargs):
        try:
            tweat = get_object_or_404(Tweet, id=id)
            queryset = self.filter_queryset(tweat)
            serializer = self.get_serializer(queryset)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id: str, *args, **kwargs):
        try:
            # get user id from token
            user = self.get_token().payload.get("user_id")
            # get tweat with id=id and author with id = user
            tweat = get_object_or_404(Tweet, id=id, author__id=user)
            queryset = self.filter_queryset(tweat)

            if queryset.author.is_active:
                tweat.delete()
                return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse(
                {"msg": "You are not authorized to make this request"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


detail = TweetDetailAPIView.as_view()


class TweetResponseLikeAPIView(BaseTweetAPIView):
    """
    User like or unlike response to tweat

    Methods:
        PUT, DELETE

    Authentication:
        Bearer Token
    """

    def put(self, request, id: str, *args, **kwargs):
        """User like tweat"""
        try:
            token = self.get_token().payload
            tweat = get_object_or_404(Tweet, id=id)
            users = get_object_or_404(User, id=token.get("user_id"))
            tweat.likes.user.add(users)
            return JsonResponse({}, status=status.HTTP_200_OK)
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id: str, *args, **kwargs):
        """User unlike tweat"""
        try:
            token = self.get_token().payload
            tweat = get_object_or_404(Tweet, id=id)
            users = get_object_or_404(User, id=token.get("user_id"))
            tweat.likes.user.remove(users)
            return JsonResponse({}, status=status.HTTP_200_OK)
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


response_like = TweetResponseLikeAPIView.as_view()


class TweetResponseCommentAPIView(BaseTweetAPIView):
    """
    User comment response to tweat

    Methods:
        POST, DELETE

    Authentication:
        Bearer Token
    """

    serializer_class = TweetResponseCommentSerializer

    def post(self, request, *args, **kwargs):
        """User post comment"""
        try:
            request = request.data.copy()
            # added user to request data
            request["user"] = self.get_token().payload.get("user_id")

            serializer = TweetResponseCommentSerializer(data=request)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """User delete comment"""
        try:
            token = self.get_token().payload.get("user_id")
            comment = get_object_or_404(
                ResponseComment, id=request.data.get("id"), user__id=token
            )

            # check if user is avtivated
            if comment.user.is_active:
                comment.delete()
                return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse(
                {"msg": "You are not authorized to make this request"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


response_comment = TweetResponseCommentAPIView.as_view()
