from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=False)
    name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ("name", "username", "avatar", "email", "password")

    def get_validation_exclusions(self):
        exclusions = super(UserSerializer, self).get_validation_exclusions()
        return exclusions + [
            "name",
            "avatar",
        ]


class UserResetActivationSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = "email"


class UserForgotPasswordSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = "password"
        read_only_fields = ["email"]


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom Token serializer to add a new data to the token that will be generated
    """

    def set_user_data(self, user):
        # check user avatar is not null
        avatar = None if bool(user.avatar) is False else user.avatar.url

        return {"username": user.username, "avatar": avatar}

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        # get token and user data
        user = self.set_user_data(self.user)
        # add extra data to the response
        data["user"] = user
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data
