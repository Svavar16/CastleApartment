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
        return '{} {} {} {}'.format(self.streetName, self.houseNumber, self.city, self.postalCode)

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
        permissions = (('can_change_price', 'Can change price'),)


class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartmentID = models.ForeignKey(Apartments, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class SearchHistoryManager(models.Manager):
    def get_by_natural_key(self, searchItem, userID):
        return self.get(searchItem=searchItem, userID=userID)

    def create_search_history(self, searchItem):
        searchItem = self.create(searchItem=searchItem)
        return searchItem

    def create_search_history_id(self, userID):
        userID = self.create(userID=userID)
        return userID


class SearchHistory(models.Model):
    objects = SearchHistoryManager()

    searchItem = models.CharField(max_length=50)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    def natural_key(self):
        return self.id, self.searchItem, self.userID,

    def __str__(self):
        return '{} {}'.format(self.searchItem, self.userID)

    class Meta:
        permissions = (('others_search_history', 'Can view others search history'),)



