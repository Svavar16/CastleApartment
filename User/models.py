from django.contrib.auth.models import User
from django.db import models
from Apartments.models import Location, Apartments


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    locationID = models.ForeignKey(Location, on_delete=models.CASCADE)


class CardDetails(models.Model):
    cardNumber = models.IntegerField(max_length=16)
    dateOfExpire = models.DateField()
    Owner = models.ForeignKey(Profile)

    def __str__(self):
        return self.cardNumber


class RealtorAgents(models.Model):
    ProfileID = models.ForeignKey(Profile)
    apartmentInChargeOf = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    dateOfCreation = models.DateField()

    def __str__(self):
        return Profile.user.first_name, Profile.user.last_name


class Customers(models.Model):
    ProfileID = models.ForeignKey(Profile)
    dateOFCreation = models.DateField()

    def __str__(self):
        return Profile.firstName, Profile.lastName


class Transaction(models.Model):
    apartmentID = models.ForeignKey(Apartments)
    cardID = models.ForeignKey(CardDetails)
    customersID = models.ForeignKey(Customers)
    realtorAgentID = models.ForeignKey(RealtorAgents)


