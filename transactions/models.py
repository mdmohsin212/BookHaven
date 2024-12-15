from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Wallet(models.Model):
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    def __str__(self):
        return self.user.username