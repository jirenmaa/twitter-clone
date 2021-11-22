import time
from typing import Any
import redis
from datetime import timedelta
from urllib.parse import quote_plus

from celeryapp.tasks import send_email_activation, send_email_resetpassword
from celeryapp.workers.mailer import email_activation_link, email_resetpassword_link
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from modules.auth.serializers import (
    AuthObtainTokenSerializer,
    AuthResetAcivationSerializer,
    AuthResetPasswordSerializer,
)
from modules.users.models import User
from modules.users.serializers import UserPublicSerializer
from modules.utility.signature import create_sha256_signature

from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    charset="utf-8",
    decode_responses=True,
)


def generate_username() -> str:
    return "enjoyer-{0}".format(str(int(round(time.time() * 1000)))[-7:])


class AuthRegistrationView(generics.CreateAPIView):
    """user registration api"""

    serializer_class = UserPublicSerializer

    def perform_create_user(self, serializer) -> str:
        """create user by given serialized data"""
        performer = User.objects.create_user(
            email=serializer.validated_data["email"],
            username=generate_username(),
            password=serializer.validated_data["password"],
        )

        return str(performer.id)

    def post(self, request, *args, **kwargs):
        """post create user
        args:
            string: email
            string: passowrd
        """
        try:
            # serialize data from request
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # create user
            performer = self.perform_create_user(serializer)
            # generate signature for user activation
            signature = create_sha256_signature(performer)

            # send email for user activation
            if settings.USE_EMAIL_BACKEND:
                send_email_activation.apply_async(
                    args=[serializer.initial_data["email"], signature],
                )
            else:
                email_activation_link(serializer.initial_data["email"], signature)

            # set redis key with signature and user id
            # and will be deleted after activation or expiration
            redis_client.set(signature, performer, timedelta(minutes=5))

            return JsonResponse(
                {"detail": "success create user"}, status=status.HTTP_201_CREATED
            )
        except ValidationError as error:
            return JsonResponse({"detail": error.detail}, status=error.status_code)
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)


class AuthActivationView(generics.CreateAPIView):
    """user activation api"""

    def delete_signature(self, signature: str) -> None:
        """delete redis key"""
        redis_client.delete(signature)

    def activate_user(self, user_id: str) -> None:
        """activate user by id"""
        performer = get_object_or_404(User, id=user_id, is_active=False)
        performer.is_active = True
        performer.save()

    def post(self, request, *args, **kwargs):
        """post user activation"""

        try:
            signature = quote_plus(request.data.get("signature"))
            # get user id from redis by signature
            performer = redis_client.get(signature)

            if not isinstance(performer, str):
                return JsonResponse(
                    {"detail": "activation expired"}, status=status.HTTP_400_BAD_REQUEST
                )

            # activate user
            self.activate_user(performer)
            # delete signature from redis
            self.delete_signature(signature)

            return JsonResponse(
                {"detail": "user acitvation successfully"},
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)


class AuthResetAcivationView(generics.GenericAPIView):
    """user reset activation api"""

    serializer_class = AuthResetAcivationSerializer

    def post(self, request, *args, **kwargs):
        """resend user activation link"""

        try:
            # serialize data from request
            serializer = self.get_serializer(data=request.data)
            # get user by email
            performer = get_object_or_404(User, email=serializer.initial_data["email"])
            # generate signature for user reset activation
            signature = create_sha256_signature(str(performer.id))

            # send email for user activation
            if settings.USE_EMAIL_BACKEND:
                send_email_activation.apply_async(
                    args=[serializer.initial_data["email"], signature],
                )
            else:
                email_activation_link(serializer.initial_data["email"], signature)

            # set redis key with signature and user id
            # and will be deleted after activation or expiration
            redis_client.set(signature, str(performer.id), timedelta(minutes=5))

            return JsonResponse(
                {"detail": "send email reset acitvation successfully"},
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)


class AuthResetPasswordView(generics.CreateAPIView):
    """user reset password api"""

    serializer_class = AuthResetPasswordSerializer

    def serialize_user(self, request) -> User:
        """get user by email"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return get_object_or_404(User, email=serializer.initial_data["email"])

    def post(self, request, *args, **kwargs):
        """request email for reset user password"""
        try:
            performer = self.serialize_user(request)

            # generate signature for user reset password
            signature = create_sha256_signature(str(performer.id))

            # send email for user activation
            if settings.USE_EMAIL_BACKEND:
                send_email_resetpassword.apply_async(
                    args=[performer.initial_data["email"], signature],
                )
            else:
                email_resetpassword_link(performer.initial_data["email"], signature)

            # set redis key with signature and user id
            # and will be deleted after activation or expiration
            redis_client.set(signature, performer, timedelta(minutes=5))

            return JsonResponse(
                {"detail": "send email reset password successfully"},
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        """reset user password"""
        try:
            signature = quote_plus(request.data.get("signature"))
            # get user id from redis by signature
            authen_id = redis_client.get(signature)

            if authen_id is None:
                return JsonResponse(
                    {"detail": "activation expired"}, status=status.HTTP_400_BAD_REQUEST
                )

            queryset = get_object_or_404(User, id=authen_id)
            # serialize data from request
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            # update user password with serialized data
            queryset.set_password(serializer.initial_data.get("password"))
            queryset.save()

            return JsonResponse(
                {"detail": "reset password successfully"}, status=status.HTTP_200_OK
            )
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)


class AuthLoginView(TokenObtainPairView):
    """user login api"""

    serializer_class = AuthObtainTokenSerializer


class AuthLogoutView(generics.GenericAPIView):
    """user logout api"""

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """user logout"""
        try:
            # Some token maybe got unautohorized when perform this action,
            # and to prevent that happend token must be refreshed and blacklisted
            # from the database
            refresh = request.data["refresh"]
            token = RefreshToken(refresh)
            token.blacklist()

            return JsonResponse({}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as ex:
            return JsonResponse({"detail": ex.args}, status=status.HTTP_400_BAD_REQUEST)


auth_registration = AuthRegistrationView.as_view()
auth_activation = AuthActivationView.as_view()
auth_resetactivation = AuthResetAcivationView.as_view()
auth_resetpassword = AuthResetPasswordView.as_view()
auth_login = AuthLoginView.as_view()
auth_logout = AuthLogoutView.as_view()
