from django.db.models.fields.files import ImageFieldFile

from modules.tweets.models import (
    ResponseComment as CommentModel,
    ResponseUserLikedTweet as UserLikedTweetModel,
    Tweet as TweetModel,
)
from modules.users.models import User

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


class AuthorTweetSerializer(serializers.HyperlinkedModelSerializer):
    """serializer for author model"""

    class Meta:
        model = User
        fields = ("name", "username", "avatar")


class TweetPublicSerializer(serializers.ModelSerializer):
    """serializer for default public tweets"""

    author = AuthorTweetSerializer()
    id = SerializerMethodField(method_name="get_model_id")
    responses = SerializerMethodField(method_name="get_responses")

    def get_model_id(self, instance: TweetModel) -> str:
        """return tweet id"""
        if isinstance(instance, CommentModel):
            return instance.tweet.id
        return instance.id

    def get_responses(self, instance: TweetModel) -> dict:
        """return responses for each tweet ('like count', 'comment count') and others"""
        if isinstance(instance, CommentModel):
            return {}

        # get user from context
        performer = self.context.get("request").auth.payload.get("user_id")
        # check if user is liked the tweet
        liked = instance.likes.user.filter(id=performer).exists()
        # check if user is commented the tweet
        commented = instance.comments.filter(author_id=performer).exists()
        # get responses counts
        count_likes = instance.likes.user.count()
        count_comments = instance.comments.count()

        return {
            "commented": commented,
            "liked": liked,
            "likes_count": count_likes,
            "comments_count": count_comments,
        }

    class Meta:
        model = TweetModel
        fields = "__all__"
        read_only_fields = ("author", "content", "responses")


class TweetPublicPostSerializer(serializers.ModelSerializer):
    """serializer for create default public tweets"""

    content = serializers.CharField(required=False, max_length=264, min_length=1)
    pictures = serializers.ImageField(required=False)

    class Meta:
        model = TweetModel
        fields = "__all__"


class TweetPublicDiscussionSerializer(serializers.ModelSerializer):
    """serializer for default public discussion for detailed tweets"""

    author = AuthorTweetSerializer()

    class Meta:
        model = CommentModel
        fields = "__all__"
        read_only_fields = ("author",)


class TweetPublicPostCommentSerializer(serializers.ModelSerializer):
    """serializer for create default public comment tweets"""

    content = serializers.CharField(required=False, max_length=264, min_length=1)
    pictures = serializers.ImageField(required=False)

    class Meta:
        model = CommentModel
        fields = "__all__"


class UserTweetPublicLikesSerializer(serializers.ModelSerializer):
    """serializer for default public user liked tweets"""

    author = AuthorTweetSerializer()
    id = SerializerMethodField(method_name="get_tweetid")
    content = SerializerMethodField(method_name="get_content")
    pictures = SerializerMethodField(method_name="get_pictures")
    responses = SerializerMethodField(method_name="get_responses")

    def get_tweetid(self, instance: UserLikedTweetModel) -> str:
        """return tweets id"""
        return str(instance.tweet.id)

    def get_content(self, instance: UserLikedTweetModel) -> str:
        """return tweets content"""
        return str(instance.tweet.content)

    def get_pictures(self, instance: UserLikedTweetModel) -> str:
        """return tweets picture"""
        return instance.tweet.pictures.url if instance.tweet.pictures else ""

    def get_responses(self, instance: UserLikedTweetModel) -> dict:
        """return responses for each tweet"""
        # get user from context
        performer = self.context.get("request").auth.payload.get("user_id")
        # check if user is liked the tweet
        liked = instance.tweet.likes.user.filter(id=performer).exists()
        # check if user is commented the tweet
        commented = instance.tweet.comments.filter(author_id=performer).exists()
        # get responses counts
        count_likes = instance.tweet.likes.user.count()
        count_comments = instance.tweet.comments.count()

        return {
            "commented": commented,
            "liked": liked,
            "likes_count": count_likes,
            "comments_count": count_comments,
        }

    class Meta:
        model = UserLikedTweetModel
        fields = "__all__"
        read_only_fields = ("id", "author", "content", "pictures", "responses",)
