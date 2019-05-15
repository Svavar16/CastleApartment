from django.db import models
from django.contrib.auth.models import User
from User.models import CardDetails
from Apartments.models import Apartments
# Create your models here.


class Transactions(models.Model):
    buyer = models.ForeignKey(User, related_name='apartment_buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='apartment_seller', on_delete=models.CASCADE)
    payment = models.ForeignKey(CardDetails, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE)

    def __str__(self):
        ret_str = '{} Buyer: {} {} Seller: {} {}'.format(str(self.apartment.locationID),
                                                       self.buyer.first_name,
                                                       self.buyer.last_name,
                                                       self.seller.first_name,
                                                       self.seller.last_name)
        return ret_str
