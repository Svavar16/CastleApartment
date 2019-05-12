from django.shortcuts import render, get_object_or_404
from Apartments.models import Apartments
from django.contrib.auth.models import User
from User.models import CardDetails
from Transactions.models import Transactions
from django.contrib import auth

# Create your views here.

def make_transaction(request, apartment_id):
    buyer = auth.get_user(request)
    apartment = get_object_or_404(Apartments, pk=apartment_id)
    seller = User.objects.get(pk=apartment.sellerID.id)
    credit_card = get_object_or_404(CardDetails, owner=buyer.id)
    transaction = Transactions(buyer=buyer, seller=seller, payment=credit_card, apartment=apartment)
    transaction.save()
    apartment.sellerID = buyer
    apartment.save()
    return render(request, 'Transactions/make_transaction.html', {
        'buyer': buyer,
        'apartment': apartment,
        'seller': seller,
        'credit_card': credit_card.cardNumber[-4:]
    })
#muna breyta apartment owner og save-a