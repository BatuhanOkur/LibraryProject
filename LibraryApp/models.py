from django.db import models
from datetime import datetime

class Author(models.Model):
    firstName = models.CharField(max_length = 50)
    secondName = models.CharField(max_length = 50)
    birthDate = models.DateField()
      
    def __str__(self):
        return self.firstName + ' ' + self.secondName
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

class Book(models.Model):
    name = models.CharField(max_length = 100)
    publishDate = models.DateField(default = datetime.now)
    createDate = models.DateField(default = datetime.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating = models.IntegerField(default = 0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
