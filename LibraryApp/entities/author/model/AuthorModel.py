from django.db import models

class Author(models.Model):
    firstName = models.CharField(max_length = 50)
    secondName = models.CharField(max_length = 50)
    birthDate = models.DateField()
      
    def __str__(self):
        return self.firstName + ' ' + self.secondName
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
