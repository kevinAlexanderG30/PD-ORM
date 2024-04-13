from django.db import models

# Create your models here.
class Autor(models.Model):  
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
