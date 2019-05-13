from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CardDetails(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    cardNumber = models.CharField(max_length=16)
    dateOfExpire = models.DateField()
    CVV = models.CharField(max_length=3)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    save = models.BooleanField()

    def __str__(self):
        return self.cardNumber




