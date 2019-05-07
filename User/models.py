from django.db import models
from Apartments.models import Location, Apartments


# Create your models here.


class Person(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    locationID = models.ForeignKey(Location, on_delete=models.CASCADE)


class CardDetails(models.Model):
    cardNumber = models.IntegerField(max_length=16)
    dateOfExpire = models.DateField()
    Owner = models.ForeignKey(Person)


class RealtorAgents(models.Model):
    PersonID = models.ForeignKey(Person)
    apartmentInChargeOf = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    dateOfCreation = models.DateField()


class Customers(models.Model):
    PersonID = models.ForeignKey(Person)
    dateOFCreation = models.DateField()


class Transaction(models.Model):
    apartmentID = models.ForeignKey(Apartments)
    cardID = models.ForeignKey(CardDetails)
    customersID = models.ForeignKey(Customers)
    realtorAgentID = models.ForeignKey(RealtorAgents)


