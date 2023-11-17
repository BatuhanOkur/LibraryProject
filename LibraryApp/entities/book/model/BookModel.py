from django.db import models
from datetime import date
from LibraryApp.entities.author.model.AuthorModel import Author

class Book(models.Model):
    name = models.CharField(max_length = 100)
    publishDate = models.DateField()
    createDate = models.DateField(default = date.today)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating = models.IntegerField(default = 0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'