from django.db import models
from User.models import Profile

# Create your models here.


class Location(models.Model):
    streetName = models.CharField(max_length=255)
    houseNumber = models.IntegerField(max_length=10)
    city = models.CharField(max_length=255)
    postalCode = models.IntegerField(max_length=10)


class Apartments(models.Model):
    price = models.FloatField(max_length=20)
    size = models.FloatField(max_length=5)
    locationID = models.ForeignKey(Location, on_delete=models.CASCADE)
    rooms = models.IntegerField(max_length=3)
    privateEntrance = models.BooleanField()
    animalsAllowed = models.BooleanField()
    garage = models.BooleanField()
    yearBuild = models.IntegerField()
    sellerID = models.ForeignKey(Profile)


class ApartmentImage(models.Model):
    candyImage = models.CharField(max_length=999)
    apartmentID = models.ForeignKey(Apartments)
