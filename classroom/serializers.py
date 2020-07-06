from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        filtrated_data = dict()

        for key in validated_data:
            filtrated_data[key] = validated_data[key]#[0]

        user = User.objects.create_user(**filtrated_data)
        return user

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password"
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=["email"]
            )
        ]