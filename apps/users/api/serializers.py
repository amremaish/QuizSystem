from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework import serializers
from django.conf import settings

from apps.users.models import User


class RestaurantAuthSerializer(serializers.ModelSerializer):
    _commercial_number = serializers.FileField(required=True)
    tax_number = serializers.CharField(required=True)
    long = serializers.FloatField(required=True)
    lat = serializers.FloatField(required=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password', 'phone', 'user_type', 'tax_number',
            '_commercial_number', 'long', 'lat')

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_username(self, value):
        if value is not None:
            return value.lower()

    def validate_email(self, value):
        if value is not None:
            return value.lower()

    @transaction.atomic
    def create(self, validated_data):
        print("sdada")
        validated_data["user_type"] = User.RESTAURANT
        validated_data["password"] = make_password(password=validated_data["password"], salt=settings.SECRET_SALT)
        return super(RestaurantAuthSerializer, self).create(validated_data)


class DriverAuthSerializer(serializers.ModelSerializer):
    _driving_license = serializers.FileField(required=False)
    _id_photo = serializers.FileField(required=False)
    _car_insurance = serializers.FileField(required=False)
    _car_registration = serializers.FileField(required=False)
    _social_security = serializers.FileField(required=False)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password', 'phone', 'user_type', '_driving_license', '_id_photo',
            '_car_insurance', '_car_registration', '_social_security')

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_username(self, value):
        if value is not None:
            return value.lower()

    def validate_email(self, value):
        if value is not None:
            return value.lower()

    @transaction.atomic
    def create(self, validated_data):
        validated_data["user_type"] = User.DRIVER
        validated_data["password"] = make_password(password=validated_data["password"], salt=settings.SECRET_SALT)
        return super(DriverAuthSerializer, self).create(validated_data)


class UpdateProfileSerializer(serializers.ModelSerializer):
    _driving_license = serializers.FileField(required=False)
    _id_photo = serializers.FileField(required=False)
    _car_insurance = serializers.FileField(required=False)
    _car_registration = serializers.FileField(required=False)
    _social_security = serializers.FileField(required=False)
    _commercial_number = serializers.FileField(required=False)
    tax_number = serializers.CharField(required=False)
    long = serializers.FloatField(required=False)
    lat = serializers.FloatField(required=False)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'phone', 'user_type', '_driving_license', '_id_photo',
            '_car_insurance', '_car_registration', '_social_security', 'user_type', 'tax_number', '_commercial_number',
            'long', 'lat')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

