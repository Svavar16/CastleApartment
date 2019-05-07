from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CardDetails(models.Model):
    cardNumber = models.IntegerField(max_length=16)
    dateOfExpire = models.DateField()
    Owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.cardNumber



