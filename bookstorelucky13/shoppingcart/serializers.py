from rest_framework import serializers
from .models import shopping_cart

class shopping_cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = shopping_cart
        fields = '__all__'