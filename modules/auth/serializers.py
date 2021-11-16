from modules.users.models import User as UserModel

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AuthResetAcivationSerializer(serializers.ModelSerializer):
    """serializer for default user reset activation serializer"""

    class Meta:
        model = UserModel
        fields = ["email"]


class AuthResetPasswordSerializer(serializers.ModelSerializer):
    """serializer for default user reset password serializer"""

    class Meta:
        model = UserModel
        fields = ["password"]
        read_only_fields = ("email")


class AuthObtainTokenSerializer(TokenObtainPairSerializer):
    """custom user obtain token serializer"""

    def set_user_data(self, user: UserModel) -> dict:
        # check user avatar is not null
        avatar = None if bool(user.avatar) is False else user.avatar.url
        return {"username": user.username, "avatar": avatar}

    def validate(self, attrs) -> dict:
        data = super().validate(attrs)
        # get token and user data
        refresh = self.get_token(self.user)
        user = self.set_user_data(self.user)

        # add extra data to the response attribute
        data["user"] = user
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data
