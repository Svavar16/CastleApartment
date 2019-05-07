from django.db import models
from Apartments.models import Location, Apartments


# Create your models here.


class Person(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    locationID = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName, self.lastName


class CardDetails(models.Model):
    cardNumber = models.IntegerField(max_length=16)
    dateOfExpire = models.DateField()
    Owner = models.ForeignKey(Person)

    def __str__(self):
        return self.cardNumber


class RealtorAgents(models.Model):
    PersonID = models.ForeignKey(Person)
    apartmentInChargeOf = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    dateOfCreation = models.DateField()

    def __str__(self):
        return Person.firstName, Person.lastName


class Customers(models.Model):
    PersonID = models.ForeignKey(Person)
    dateOFCreation = models.DateField()

    def __str__(self):
        return Person.firstName, Person.lastName


class Transaction(models.Model):
    apartmentID = models.ForeignKey(Apartments)
    cardID = models.ForeignKey(CardDetails)
    customersID = models.ForeignKey(Customers)
    realtorAgentID = models.ForeignKey(RealtorAgents)


