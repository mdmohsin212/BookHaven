from django.db import models
from django.contrib.auth.models import User
from categories.models import Categorie

# Create your models here.

class BookModel(models.Model):
    name = models.CharField(max_length=100)
    des = models.TextField()
    user = models.ManyToManyField(User, blank=True)
    image = models.ImageField(upload_to='uploads/')
    price = models.IntegerField()
    category = models.ManyToManyField(Categorie, blank=True)
    
    
    def __str__(self):  
        return self.name
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    createdate=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.book.name