from django.shortcuts import render, get_object_or_404
from Apartments.models import Apartments
from django.contrib.auth.models import User
from User.models import CardDetails
from Transactions.models import Transactions

# Create your views here.

def make_transaction(request, apartment_id):
    buyer = request.user
    apartment = get_object_or_404(Apartments, pk=apartment_id)
    seller = apartment.sellerID
    credit_card = get_object_or_404(CardDetails, owner=buyer)
    transaction = Transactions(buyer, seller, credit_card, apartment)
    transaction.save()
    apartment.sellerID = buyer
    apartment.save()
#muna breyta apartment owner og save-a