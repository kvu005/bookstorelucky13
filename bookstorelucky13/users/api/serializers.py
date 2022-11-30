from rest_framework import serializers
from users.models import User


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]


class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'home_address']


class UpdateUserSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(required=False)
    password = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    home_address = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ["username", "password", "name", "home_address"]


class UserCrediSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]
