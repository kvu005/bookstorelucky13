from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from cards.api.serializers import BaseCreditCardSerializer
from users.models import User
from cards.models import CreditCard

class CreditCardViewSet(viewsets.ViewSet):

    def create(self, request: Request) -> BaseCreditCardSerializer:
        serializer = BaseCreditCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(username=serializer.data.get("user")).first()
        if not user:
            raise APIException("No user found.")

        card = CreditCard.objects.create(**{**serializer.data, "user": user})
        serializer = BaseCreditCardSerializer(card)
        return Response(serializer.data)
