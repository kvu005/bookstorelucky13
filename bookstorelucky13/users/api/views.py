from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from users.api.serializers import BaseUserSerializer, CreateUserSerializer, UpdateUserSerializer
from cards.api.serializers import BaseCreditCardSerializer

from users.models import User


class UserViewSet(viewsets.ViewSet):
    lookup_field = 'username'
    lookup_value_regex = '[0-9a-z\.@]+'

    def create(self, request: Request) -> BaseUserSerializer:
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user: User = serializer.save()
        # password = request.data.pop('password')
        # user.set_password(password)
        user.save()

        response = BaseUserSerializer(user)
        return Response(response.data)

    def retrieve(self, request: Request, username: str | None = None) -> BaseUserSerializer:
        user = User.objects.filter(username=username).first()
        if not user:
            raise APIException(detail="No user found.")
        serializer = BaseUserSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request: Request, username: str | None = None) -> BaseUserSerializer:
        user = User.objects.filter(username=username).first()
        if not user:
            raise APIException(detail="No user found.")

        serializer = UpdateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if (password := serializer.data.pop('password', None)):
            # user.set_password(password)
            user.save()

        User.objects.filter(id=user.id).update(**serializer.data)

        user.refresh_from_db()
        response = BaseUserSerializer(user)
        return Response(response.data)

    @action(detail=True, methods=["GET"])
    def creditcards(self, request: Request, username: str | None = None) -> BaseCreditCardSerializer:
        user = User.objects.filter(username=username).first()
        if not user:
            raise APIException(detail="No user found.")
        serializer = BaseCreditCardSerializer(user.cards.all(), many=True)
        return Response(serializer.data)
