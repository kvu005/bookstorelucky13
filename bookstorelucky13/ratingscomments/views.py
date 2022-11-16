from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Authors, Books, Users, Comments, Ratings
from .serializers import AuthorsSerializer, BooksSerializer, UsersSerializer, CommentsSerializer, RatingsSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

    elif request.metohd == 'PUT':
        author_data = JSONParser().parse(request)
        author_serializer = AuthorsSerializer(author, data=author_data)
        if author_serializer.is_valid():
            author_serializer.save()
            return JsonResponse(author_serializer.data)
        return JsonResponse(author_serializer.errors, status=400)

    elif request.method == 'DELETE':
        author.delete()
        return HttpResponse(status=204)

# Views for Books

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
        book = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        book_serializer = BooksSerializer(book)
        return JsonResponse(book_serializer.data)

    elif request.metohd == 'PUT':
        book_data = JSONParser().parse(request)
        book_serializer = BooksSerializer(book, data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data)
        return JsonResponse(book_serializer.errors, status=400)

    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)

# Views for Users

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        user = Users.objects.all()
        user_serializer = UsersSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=201)
        return JsonResponse(user_serializer.errors, status=400)

@csrf_exempt
def user_detail(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        user_serializer = UsersSerializer(user)
        return JsonResponse(user_serializer.data)

    elif request.metohd == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

# Views for Comments

@csrf_exempt
def comment_list(request):
    if request.method == 'GET':
        comment = Comments.objects.all()
        comment_serializer = CommentsSerializer(comment, many=True)
        return JsonResponse(comment_serializer.data, safe=False)
    
    elif request.method == 'POST':
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentsSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data, status=201)
        return JsonResponse(comment_serializer.errors, status=400)

@csrf_exempt
def comment_detail(request, pk):
    try:
        comment = Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        comment_serializer = CommentsSerializer(comment)
        return JsonResponse(comment_serializer.data)

    elif request.metohd == 'PUT':
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentsSerializer(comment, data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data)
        return JsonResponse(comment_serializer.errors, status=400)

    elif request.method == 'DELETE':
        comment.delete()
        return HttpResponse(status=204)

# Views for Ratings

@csrf_exempt
def rating_list(request):
    if request.method == 'GET':
        rating = Ratings.objects.all()
        rating_serializer = RatingsSerializer(rating, many=True)
        return JsonResponse(rating_serializer.data, safe=False)
    
    elif request.method == 'POST':
        rating_data = JSONParser().parse(request)
        rating_serializer = RatingsSerializer(data=rating_data)
        if rating_serializer.is_valid():
            rating_serializer.save()
            return JsonResponse(rating_serializer.data, status=201)
        return JsonResponse(rating_serializer.errors, status=400)

@csrf_exempt
def rating_detail(request, pk):
    try:
        rating = Ratings.objects.get(pk=pk)
    except Ratings.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        rating_serializer = RatingsSerializer(rating)
        return JsonResponse(rating_serializer.data)

    elif request.metohd == 'PUT':
        rating_data = JSONParser().parse(request)
        rating_serializer = RatingsSerializer(rating, data=rating_data)
        if rating_serializer.is_valid():
            rating_serializer.save()
            return JsonResponse(rating_serializer.data)
        return JsonResponse(rating_serializer.errors, status=400)

    elif request.method == 'DELETE':
        rating.delete()
        return HttpResponse(status=204)