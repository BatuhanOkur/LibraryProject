from LibraryApp.entities.author.model.AuthorModel import Author
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=('firstName','secondName', 'birthDate')
