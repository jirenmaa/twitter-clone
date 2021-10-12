from django.http import JsonResponse

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken


class BaseUserApiView(GenericAPIView):
    """User Base API view"""

    permission_classes = (IsAuthenticated,)

    def get_token(self):
        # get bearer token from request
        tokens = self.request.META.get("HTTP_AUTHORIZATION", " ").split()[-1]
        # get access token from bearer token
        access = AccessToken(tokens)
        return access


class UserTweatsApiView(BaseUserApiView):
    """Retrive all user created tweats"""

    def get(self, request, *args, **kwargs):
        # get user id from access token
        user_id = self.get_token().payload.get("user_id")
        # get all tweats from user
        user_tweats = []
