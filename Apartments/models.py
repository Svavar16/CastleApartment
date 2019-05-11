from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class LocationManager(models.Manager):
    def get_by_natural_key(self, streetName, houseNumber, city, postalCode):
        return self.get(streetName=streetName, houseNumber=houseNumber, city=city, postalCode=postalCode)


class Location(models.Model):
    objects = LocationManager()

    streetName = models.CharField(max_length=255)
    houseNumber = models.IntegerField()
    city = models.CharField(max_length=255)
    postalCode = models.IntegerField()

    def natural_key(self):
        return self.id, self.streetName, self.houseNumber, self.city, self.postalCode

    def __str__(self):
        return self.streetName, self.houseNumber, self.city, self.postalCode

    class Meta:
        unique_together = (('streetName', 'houseNumber', 'city', 'postalCode'),)


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
    forSale = models.BooleanField()
    class Meta:
        permissions = (('can change_price', 'Can change price'),)


class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartmentID = models.ForeignKey(Apartments, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
