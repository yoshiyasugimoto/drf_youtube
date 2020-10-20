from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Video


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        field = ("email", "password", "username", "id")
        extra_kwargs = {"password": {"write_only": True, 'min_length': 5}}
