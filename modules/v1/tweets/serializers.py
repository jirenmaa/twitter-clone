from django_bleach.models import BleachField

from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import SerializerMethodField

from modules.v1.users.models import User
from modules.v1.tweets.models import Tweet, ResponseComment, ResponseLike
from modules.utils import linkify


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Author model"""

    class Meta:
        model = User
        fields = ("name", "username", "avatar")


class TweetSerializer(serializers.ModelSerializer):
    """Serializer for tweet default"""

    author = AuthorSerializer()
    content = SerializerMethodField(method_name="get_content")
    responses = SerializerMethodField(method_name="get_responses")

    def get_content(self, instance):
        return linkify.linkify_content(instance.content)

    def get_responses(self, instance):
        a = self
        # get user id from context request
        user = self.context.get("request").auth.payload.get("user_id")
        # check if current user is liked the tweet
        liked = instance.likes.user.filter(id=user).exists()
        # check if current user is commented the tweet
        commented = instance.comments.filter(user__id=user).exists()
        # get likes count
        likes_count = instance.likes.user.count()
        # get comments count
        comments_count = instance.comments.count()

        return {
            "liked": liked,
            "commented": commented,
            "likes_count": likes_count,
            "comments_count": comments_count,
        }

    class Meta:
        model = Tweet
        fields = "__all__"
        read_only_fields = ["author", "content", "responses"]


class TweetDetailSerializer(serializers.ModelSerializer):
    """Serializer for detailed tweet"""

    author = AuthorSerializer()
    content = SerializerMethodField(method_name="get_content")
    responses = SerializerMethodField(method_name="get_responses")

    def get_content(self, instance):
        return linkify.linkify_content(instance.content)

    def get_responses(self, instance):
        # get user id from context request
        user = self.context.get("request").auth.payload.get("user_id")
        # check if current user is liked the tweet
        liked = instance.likes.user.filter(id=user).exists()
        # check if current user is commented the tweet
        commented = instance.comments.filter(user__id=user).exists()
        # get likes count
        likes_count = instance.likes.user.count()
        # get comments count
        comments_count = instance.comments.count()
        # get comments
        comments = TweetDetailCommentSerializer(
            instance.comments.all(), many=True, context={"request": self.context}
        ).data

        return {
            "liked": liked,
            "commented": commented,
            "likes_count": likes_count,
            "comments_count": comments_count,
            "comments": comments,
        }

    class Meta:
        model = Tweet
        fields = "__all__"
        read_only_fields = ["author", "content", "responses"]


class TweetPostSerializer(serializers.ModelSerializer):
    """Serializer for creating tweet"""

    content = serializers.CharField(required=False, max_length=264, min_length=1)
    picture = serializers.ImageField(required=False)

    class Meta:
        model = Tweet
        fields = "__all__"


class TweetResponseCommentSerializer(serializers.ModelSerializer):
    """Serializer for POST comment"""

    content = BleachField(max_length=264)

    class Meta:
        model = ResponseComment
        fields = "__all__"


class TweetResponseLikeSerializer(serializers.ModelSerializer):
    """Serializer for POST like"""

    user = AuthorSerializer()

    class Meta:
        model = ResponseLike
        fields = "__all__"


class TweetDetailCommentSerializer(serializers.ModelSerializer):
    """Serializer for detailed tweet comment"""

    user = AuthorSerializer()

    class Meta:
        model = ResponseComment
        fields = "__all__"
        read_only_fields = ["user"]
