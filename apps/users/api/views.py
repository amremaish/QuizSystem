from datetime import datetime

from django.contrib.auth.hashers import make_password
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.common.custom_response import success, error
from django.conf import settings

from apps.users.api import serializers
from apps.users.models import User

class DriverSignUpView(CreateAPIView):
    serializer_class = serializers.DriverAuthSerializer
    permission_classes = (AllowAny,)


class RestaurantSignUpView(CreateAPIView):
    serializer_class = serializers.RestaurantAuthSerializer
    permission_classes = (AllowAny,)


class UpdateProfileView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UpdateProfileSerializer

    def put(self, request):
        serializer = self.serializer_class(instance=request.user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CurrentUserView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        data = User.objects.filter(email=request.user).values()[0]
        data['password'] = None
        return Response(data, status=status.HTTP_200_OK)



class UpdateDriverLocation(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        driver = User.objects.filter(id=request.user.id).first()
        driver.long = request.data.get('long')
        driver.lat = request.data.get('lat')
        driver.last_location_date = datetime.now()
        driver.save()
        return Response(success('Location updated successfully'), status=status.HTTP_200_OK)


class ChangeUserPassword(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = User.objects.filter(id=request.user.id).first()
        old_password = request.data.get('old_password')

        if user.password == make_password(password=old_password, salt=settings.SECRET_SALT):
            user.password = make_password(password=request.data.get('new_password'), salt=settings.SECRET_SALT)
            user.save()
            return Response(success('Password changed successfully'), status=status.HTTP_200_OK)
        return Response(error('Old Password is Wrong'), status=status.HTTP_400_BAD_REQUEST)

