from rest_framework import serializers

from QuizSystem.settings import REST_FRAMEWORK


class PageSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, default=1)
    size = serializers.IntegerField(required=False, max_value=100, default=REST_FRAMEWORK['PAGE_SIZE'])
    q = serializers.CharField(required=False, default="")
    status = serializers.CharField(required=False, default="")
