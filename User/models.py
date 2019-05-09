from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CardDetails(models.Model):
    cardNumber = models.IntegerField()
    dateOfExpire = models.DateField()
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cardNumber



