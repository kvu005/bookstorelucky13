from rest_framework import serializers
from .models import Authors, Books, Users, Comments, Ratings

class AuthorsSerializer(serializers.ModelSerializer):
    class meta:
        model = Authors
        fields = '__all__'

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'