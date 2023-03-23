from django.contrib.auth.models import User
from rest_framework import serializers

from .models import TelegramUser


class TelegramUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    is_bot = serializers.BooleanField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255, allow_blank=True)
    username = serializers.CharField(max_length=255, allow_blank=True)
    language_code = serializers.CharField(max_length=50, allow_blank=True)

    def validate_is_bot(self, value):
        if value:
            raise serializers.ValidationError("Cannot process messages from the bot")

        return value
