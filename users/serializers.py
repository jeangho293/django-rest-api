from rest_framework import serializers
from users.models import User
from bcrypt import gensalt, hashpw, checkpw


# Serializer를 적용하면 DB데이터가 dict형태로 변환된다.
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    account = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["id", "account", "password"]

    @staticmethod
    def find_one(**filter_options) -> User:
        return User.manager.find_one(**filter_options)

    def create(self, validated_data):
        account: str = validated_data.get("account")
        password: str = validated_data.get("password")

        hashed_password = hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")
        return User.manager.create(account=account, password=hashed_password)
