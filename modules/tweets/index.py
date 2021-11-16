from typing import List, Tuple

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from modules.tweets.models import ResponseComment, ResponseUserLikedTweet, Tweet
from modules.tweets.serializers import (
    TweetPublicSerializer,
    TweetPublicPostSerializer,
    TweetPublicPostCommentSerializer,
    TweetPublicDiscussionSerializer,
)
from modules.users.models import User

from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken


class TweetBaseApi(generics.GenericAPIView):
    """base class for public tweet api views"""

    permission_classes = (IsAuthenticated,)
    serializer_class = None

    def get_queryset(self) -> Tweet:
        pass

    def retrive_token(self, request) -> AccessToken:
        """get token from authorization header"""
        tokens = request.META.get("HTTP_AUTHORIZATION", " ").split()[-1]
        access = AccessToken(tokens)
        return access

    def update_request(self, request):
        """add 'user id' into request data"""
        copied_request = request.data.copy()
        copied_request["author"] = self.retrive_token(request).payload.get("user_id")

        return copied_request


class TweetPublicView(TweetBaseApi):
    """public tweet api views
    methods: get, post
    """

    serializer_class = TweetPublicSerializer

    def get_queryset(self) -> List[Tweet]:
        """return list of tweet"""
        return Tweet.objects.all().order_by("-created_at")

    def list(self, request, *args, **kwargs):
        """return list of tweet with pagination"""
        try:
            # serialize data from database and paginate
            # by default, paginate by 10
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)

            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        """return list of tweet"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """create new tweet"""
        try:
            request = self.update_request(request)
            # serialize data from request
            serializer = TweetPublicPostSerializer(data=request)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # return data
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)


class TweetDetailView(TweetBaseApi):
    """public detail tweet api views
    methods: get, delete
    """

    serializer_class = TweetPublicSerializer

    def get_queryset(self, id: str) -> Tweet:
        """return queryset of tweet"""
        object = get_object_or_404(Tweet, pk=id)
        queryset = self.filter_queryset(object)

        return queryset

    def get(self, request, id: str, *args, **kwargs):
        """return detail tweet"""
        try:
            queryset = self.get_queryset(id)
            serializer = self.get_serializer(queryset)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id: str, *args, **kwargs):
        """delete tweet"""
        try:
            # get user from authorization header
            performer = self.retrive_token(request).user.id
            # get tweet queryset
            tweet = get_object_or_404(
                Tweet, pk=id, author__id=performer, author__is_active=True
            )
            queryset = self.filter_queryset(tweet)

            # delete tweet if user is active
            if queryset.author.is_active:
                tweet.delete()
                return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse(
                {"detail": "you are not authorized to perform this request"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)


class TweetResponseView(TweetBaseApi):
    """response comment disscussion for detailed tweet"""

    serializer_class = TweetPublicDiscussionSerializer

    def get_queryset(self, id: str) -> List[Tweet]:
        """return queryset of tweet response"""
        object = get_object_or_404(Tweet, pk=id)
        queryset = self.filter_queryset(object.comments.all())

        return queryset

    def get(self, request, id: str, *args, **kwargs):
        """return replies of tweet response"""
        try:
            queryset = self.get_queryset(id)
            serializer = self.get_serializer(queryset, many=True)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)


class TweetResponseLikeView(TweetBaseApi):
    """response like or unlike tweet
    methods: put, delete
    """

    def is_already_liked(
        self, request, tweet: Tweet
    ) -> Tuple[ResponseUserLikedTweet, User]:
        """return queryset of user liked tweet"""
        token = self.retrive_token(request).payload
        performer = get_object_or_404(User, pk=token.get("user_id"))
        # get user liked tweet
        liked = ResponseUserLikedTweet.objects.filter(tweet=tweet, author=performer)

        return liked, performer

    def put(self, request, id: str, *args, **kwargs):
        """like tweet response"""
        try:
            tweet = get_object_or_404(Tweet, pk=id)
            already_liked, performer = self.is_already_liked(request, tweet)

            if not already_liked.exists():
                # append user to liked tweet
                tweet.likes.user.add(performer)
                # add liked tweet to user liked tweet
                liked_by = ResponseUserLikedTweet(tweet=tweet, author=performer)
                liked_by.save()
            return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id: str, *args, **kwargs):
        """unlike tweet response"""
        try:
            tweet = get_object_or_404(Tweet, pk=id)
            already_liked, performer = self.is_already_liked(request, tweet)

            if already_liked.exists():
                # delete user from liked tweet
                tweet.likes.user.remove(performer)
                # delete user liked tweet
                already_liked.delete()
            return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)


class TweetResponseReplyView(TweetBaseApi):
    """create comment of tweet response
    methods: post, delete
    """

    serializer_class = TweetPublicPostCommentSerializer

    def post(self, request, *args, **kwargs):
        """create replies"""
        try:
            request = self.update_request(request)
            # create user replied tweet
            serializer = self.serializer_class(data=request)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """delete replies"""
        try:
            # get user from authorization header
            performer = self.retrive_token(request).payload.get("user_id")
            # get tweet response queryset
            response = get_object_or_404(
                ResponseComment,
                pk=request.data.get("id"),
                author__id=performer,
                author__is_active=True,
            )
            queryset = self.filter_queryset(response)

            # delete response if user is active
            if queryset.author.is_active:
                response.delete()
                return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
            return JsonResponse(
                {"detail": "you are not authorized to perform this request"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)


tweet_public = TweetPublicView.as_view()
tweet_detail = TweetDetailView.as_view()
tweet_responses = TweetResponseView.as_view()
tweet_responses_like = TweetResponseLikeView.as_view()
tweet_responses_reply = TweetResponseReplyView.as_view()
