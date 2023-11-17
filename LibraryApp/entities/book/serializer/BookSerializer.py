from LibraryApp.entities.book.model.BookModel import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('name','author', 'publishDate', 'createDate', 'rating')