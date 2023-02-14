from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    account = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return User.manager.create(**validated_data)