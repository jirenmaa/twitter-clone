from modules.users.models import User as UserModel

from rest_framework import serializers


class UserPublicSerializer(serializers.ModelSerializer):
    """serializer for default user serializer"""

    avatar = serializers.ImageField(required=False)
    name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)

    class Meta:
        model = UserModel
        fields = ("name", "username", "avatar", "email", "password")


class UserPublicInfoSerializer(serializers.ModelSerializer):
    """serializer for default user info serializer"""

    class Meta:
        model = UserModel
        fields = ("name", "username", "avatar")
