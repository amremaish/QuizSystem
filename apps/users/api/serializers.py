
from rest_framework import serializers


class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    repeat_password = serializers.CharField()
