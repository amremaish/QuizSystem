from django.contrib.auth.hashers import make_password
from rest_framework import status, permissions
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from QuizSystem import settings
from apps.users.api import serializers
from apps.users.models import User


class AuthView(CreateAPIView):
    serializer_class = serializers.AuthSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        if data.get('repeat_password') != data.get('password'):
            raise APIException("Password and repeat password doesn't the same")
        old = User.objects.filter(email=data.get('email'))
        if old:
            raise APIException("Email is already existing")
        user = User(
            password=make_password(password=data["password"], salt=settings.SECRET_SALT),
            username=data['email'],
            email=data['email']
        )
        user.save()
        return Response({"status": status.HTTP_200_OK, "details": user.email})


class CurrentUserView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return Response({"status": status.HTTP_200_OK, "details": {"email": request.user.email}})
