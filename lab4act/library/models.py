from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
      
    def __str__(self) -> str:
        return self.first_name + "  " + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=100, null=True)
    pages= models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price= models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self) -> str:
        return self.title
    

