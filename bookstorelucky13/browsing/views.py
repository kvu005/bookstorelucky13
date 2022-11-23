from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Authors, Books
from .serializers import AuthorsSerializer, BooksSerializer
#from django.db import models
#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response

# Create your views here.

#views for authors

@csrf_exempt
def author_list(request):
    if request.method == 'GET':
        author = Authors.objects.all()
        author_serializer = AuthorsSerializer(author, many=True)
        return JsonResponse(author_serializer.data, safe=False)

    elif request.method == 'POST':
        author_data = JSONParser().parse(request)
        author_serializer = AuthorsSerializer(data=author_data)
        if author_serializer.is_valid():
            author_serializer.save()
            return JsonResponse(author_serializer.data, status=201)
        return JsonResponse(author_serializer.errors, status=400)

@csrf_exempt
def author_detail(request, pk):
    try:
        author = Authors.objects.get(pk=pk)
    except Authors.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        author_serializer = AuthorsSerializer(author)
        return JsonResponse(author_serializer.data)

    elif request.method == 'PUT':
        author_data = JSONParser().parse(request)
        author_serializer = AuthorsSerializer(author, data=author_data)
        if author_serializer.is_valid():
            author_serializer.save()
            return JsonResponse(author_serializer.data)
        return JsonResponse(author_serializer.errors, status=400)

    elif request.method == 'DELETE':
        author.delete()
        return HttpResponse(status=204)

#views for books

@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        book = Books.objects.all()
        book_serializer = BooksSerializer(book, many=True)
        return JsonResponse(book_serializer.data, safe=False)

    elif request.method == 'POST':
        book_data = JSONParser().parse(request)
        book_serializer = BooksSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data, status=201)
        return JsonResponse(book_serializer.errors, status=400)

@csrf_exempt
def book_detail(request, pk):
    try:
        book = Books.objects.get(AuthorName_id=pk)
    except Books.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        book_serializer = BooksSerializer(book)
        return JsonResponse(book_serializer.data)
    elif request.method == 'PUT':
        book_data = JSONParser().parse(request)
        book_serializer = BooksSerializer(book, data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data)
        return JsonResponse(book_serializer.errors, status=400)

    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)

@csrf_exempt
def genre(request,feature):
    try: 
        book = Books.objects.filter(Genere=feature)
    except:
         return HttpResponse(status=404)
    if request.method == 'GET':
        book_serializer = BooksSerializer(book, many=True)
        return JsonResponse(book_serializer.data, safe=False)

@csrf_exempt
def top_seller(request):
    try: 
        book = Books.objects.all().order_by('-CopiesSold')[:5]
    except:
         return HttpResponse(status=404)
    if request.method == 'GET':
        book_serializer = BooksSerializer(book, many=True)
        return JsonResponse(book_serializer.data, safe=False)
@csrf_exempt
def rating(request, feature):
    try:
        book = Books.objects.filter(AvgRating__gte = feature).order_by('-AvgRating')
    except:
         return HttpResponse(status=404)
    if request.method == 'GET':
        book_serializer = BooksSerializer(book, many=True)
        return JsonResponse(book_serializer.data, safe=False)
def position(request,feature,pk):
    try:
        book = Books.objects.filter(AuthorName_id__gte=pk)[:feature]
    except:
        return HttpResponse(status=404)
    if request.method =='GET':
            book_serializer = BooksSerializer(book, many=True)
            return JsonResponse(book_serializer.data, safe=False)
