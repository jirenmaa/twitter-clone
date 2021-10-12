from datetime import timedelta
from urllib.parse import quote_plus

import redis
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from tasks import tasks
from modules.utils.url_signature import create_sha256_signature
from modules.v1.users.models import User
from modules.v1.users.serializers import (
    UserRestActivationSerializer,
    UserSerializer,
    UserTokenObtainPairSerializer,
)

from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

redis_client = redis.Redis(
    host="localhost", port=6379, db=0, charset="utf-8", decode_responses=True
)


class AuthRegisterAPIView(generics.CreateAPIView):
    """User registration view"""

    serializer_class = UserSerializer

    def perform_create_user(self, serializer):
        """
        Perform user creation with validated data from serializer
        """
        user = User.objects.create_user(
            email=serializer.validated_data["email"],
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        return str(user.id)

    def post(self, request, *args, **kwargs):
        """
        Create user
        """
        try:
            # validate data from request
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # perform user creation
            user = self.perform_create_user(serializer)
            # generate url signature
            url_signature = create_sha256_signature(user)
            # send activation email
            tasks.send_mail_queue.apply_async(
                args=[
                    request.scheme,
                    request.get_host(),
                    serializer.validated_data["email"],
                    url_signature,
                ]
            )

            # url signature for user activation is stored in redis for 5 minutes
            # and deleted after activation or expiration
            redis_client.set(url_signature, user, timedelta(minutes=5))

            return JsonResponse(
                serializer.validated_data, status=status.HTTP_201_CREATED
            )
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


register = AuthRegisterAPIView.as_view()


class AuthActivateAPIView(generics.GenericAPIView):
    """User activation view"""

    def get(self, request, *args, **kwargs):
        """
        Activate user
        """
        try:
            # get url signature from request
            # escape key that it can contain special characters
            # because it is used as key in redis
            key = quote_plus(request.GET.get("key"))
            # get user id from url signature
            user_id = redis_client.get(key)

            # if user id is not found in redis
            # it means that user is already activated or maybe expired
            if user_id is None:
                return JsonResponse(
                    {"msg": "User activation link expired"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # activate user
            user = User.objects.get(id=user_id)
            user.is_active = True
            user.save()

            # delete url signature from redis after activation
            redis_client.delete(key)
            return JsonResponse(
                {"msg": "user successfully activated"},
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


activate = AuthActivateAPIView.as_view()


class AuthResetActivationAPIView(generics.GenericAPIView):
    """User reset activation url view"""

    serializer_class = UserRestActivationSerializer

    def get(self, request, *args, **kwargs):
        """
        Reset user activation
        """
        try:
            # validate data from request
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # get user, and because the serializer is not saved
            # so it use the inital_data from serializer instead of validated_data
            user = get_object_or_404(User, email=serializer.initial_data["email"])
            # generate url signature
            url_signature = create_sha256_signature(str(user.id))
            # send reset activation email
            tasks.send_mail_queue.apply_async(
                args=[
                    request.scheme,
                    request.get_host(),
                    serializer.initial_data["email"],
                    url_signature,
                ]
            )

            # url signature for user activation is stored in redis for 5 minutes
            # and deleted after activation or expiration
            redis_client.set(url_signature, str(user.id), timedelta(minutes=5))

            return JsonResponse(
                {"msg": "Reset activation email sent"}, status=status.HTTP_200_OK
            )
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


reset_activation = AuthResetActivationAPIView.as_view()


class AuthLogin(TokenObtainPairView):
    """User login view, return (refresh, access) token for the user"""

    serializer_class = UserTokenObtainPairSerializer


login = AuthLogin.as_view()


class AuthLogout(GenericAPIView):
    """User logout view, return empty response"""

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        # Some token maybe got unautohorized when perform this action,
        # and to prevent that happend token must be refreshed and blacklisted
        # from the database
        try:
            refresh = request.data["refresh"]
            token = RefreshToken(refresh)
            token.blacklist()

            return JsonResponse({}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as ex:
            return JsonResponse({"msg": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


logout = AuthLogout.as_view()
