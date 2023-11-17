from django.contrib import admin
from LibraryApp.entities.book.model.BookModel import Book
from LibraryApp.entities.author.model.AuthorModel import Author

admin.site.register(Book)
admin.site.register(Author)
