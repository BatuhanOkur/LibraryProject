from rest_framework import viewsets
from LibraryApp.entities.author.model.AuthorModel import Author
from LibraryApp.entities.author.serializer.AuthorSerializer import AuthorSerializer
from rest_framework.response import Response
from rest_framework import serializers

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer