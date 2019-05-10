from django.db import models
from django.contrib.auth.models import User
from User.models import CardDetails
from Apartments.models import Apartments
# Create your models here.


class Transactions(models.Model):
    buyer = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    seller = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    payment = models.OneToOneField(CardDetails, on_delete=models.DO_NOTHING)
    apartment = models.OneToOneField(Apartments, on_delete=models.DO_NOTHING)
