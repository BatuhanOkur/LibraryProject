from libraryapp.models import Author, Book
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=('firstName','secondName', 'birthDate')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('name','author', 'publishDate', 'createDate', 'rating')