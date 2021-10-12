from django_bleach.models import BleachField

from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import SerializerMethodField

from modules.v1.users.models import User
from modules.v1.tweets.models import Tweet, ResponseComment
from modules.utils import linkify


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Author model"""

    class Meta:
        model = User
        fields = ("name", "username", "avatar")


class AuthorCommentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Author model"""

    class Meta:
        model = User
        fields = ("id",)


class TweetSerializer(serializers.ModelSerializer):
    """Serializer for tweet default"""

    author = AuthorSerializer()
    content = SerializerMethodField(method_name="get_content")

    def get_content(self, instance):
        return linkify.linkify_content(instance.content)

    class Meta:
        model = Tweet
        fields = "__all__"
        read_only_fields = ["author", "content"]


class TweetPostSerializer(serializers.ModelSerializer):
    """Serializer for creating tweet"""

    content = serializers.CharField(required=False, max_length=264, min_length=1)
    picture = serializers.ImageField(required=False)

    class Meta:
        model = Tweet
        fields = "__all__"


class TweetResponseCommentSerializer(serializers.ModelSerializer):
    content = BleachField(max_length=264)

    class Meta:
        model = ResponseComment
        fields = "__all__"
