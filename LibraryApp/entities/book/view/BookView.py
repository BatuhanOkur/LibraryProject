from rest_framework import viewsets
from LibraryApp.entities.book.model.BookModel import Book
from LibraryApp.entities.book.serializer.BookSerializer import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer