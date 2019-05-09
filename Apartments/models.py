from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):
    streetName = models.CharField(max_length=255)
    houseNumber = models.IntegerField()
    city = models.CharField(max_length=255)
    postalCode = models.IntegerField()

    def __str__(self):
        return self.streetName, self.houseNumber


class Apartments(models.Model):
    price = models.FloatField()
    size = models.FloatField()
    locationID = models.ForeignKey(Location, on_delete=models.CASCADE)
    rooms = models.IntegerField()
    privateEntrance = models.BooleanField()
    animalsAllowed = models.BooleanField()
    garage = models.BooleanField()
    yearBuild = models.IntegerField()
    description = models.CharField(max_length=999)
    sellerID = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        permissions = (('can change_price', 'Can change price'),)


class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartmentID = models.ForeignKey(Apartments, on_delete=models.CASCADE)

    def __str__(self):
        return self.candyImage
