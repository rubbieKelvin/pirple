from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer, UserSerializer

class UserCreateSerializerCustom(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name"
        ]