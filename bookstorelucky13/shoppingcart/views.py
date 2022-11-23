from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import shopping_cart
from .serializers import shopping_cartSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

#views for authors

@csrf_exempt
def shopping_cart_list(request):
    if request.method == 'GET':
        shoppingCart = shopping_cart.objects.all()
        shopping_cart_serializer = shopping_cartSerializer(shoppingCart, many = True)
        return JsonResponse(shopping_cart_serializer.data, safe = False)

    elif request.method == 'POST':
        shopping_cart_data = JSONParser().parse(request)
        shopping_cart_serializer = shopping_cartSerializer(data = shopping_cart_data)
        if shopping_cart_serializer.is_valid():
            shopping_cart_serializer.save()
            return JsonResponse(shopping_cart_serializer.data, status = 201)
        return JsonResponse(shopping_cart_serializer.errors, status = 400)

@csrf_exempt
def shopping_cart_detail(request, pk):
    try:
        shoppingCart = shopping_cart.objects.get(pk=pk)
    except shopping_cart.DoesNotExist:
        return HttpResponse(status=404)
 
    if request.method == 'GET':
        shopping_cart_serializer = shopping_cartSerializer(shoppingCart)
        return JsonResponse(shopping_cart_serializer.data)
 
    elif request.method == 'PUT':
        shopping_cart_data = JSONParser().parse(request)
        shopping_cart_serializer = shopping_cartSerializer(shoppingCart, data=shopping_cart_data)
        if shopping_cart_serializer.is_valid():
            shopping_cart_serializer.save()
            return JsonResponse(shopping_cart_serializer.data)
        return JsonResponse(shopping_cart_serializer.errors, status=400)
 
    elif request.method == 'DELETE':
        shoppingCart.delete()
        return HttpResponse(status=204)