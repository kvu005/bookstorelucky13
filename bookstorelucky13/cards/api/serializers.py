from rest_framework import serializers
from cards.models import CreditCard


class BaseCreditCardSerializer(serializers.ModelSerializer):
    user = serializers.EmailField()
    class Meta:
        model = CreditCard
        fields = '__all__'
