from django.shortcuts import render, get_object_or_404
from Apartments.models import Apartments
from django.contrib.auth.models import User
from User.models import CardDetails
from Transactions.models import Transactions
from django.contrib import auth
from User.forms.select_card import SelectCardForm

# Create your views here.

def make_transaction(request, apartment_id, payment_id):
    buyer = auth.get_user(request)
    apartment = get_object_or_404(Apartments, pk=apartment_id)
    seller = User.objects.get(pk=apartment.sellerID.id)
    credit_card = get_object_or_404(CardDetails, pk=payment_id)
    if credit_card.ower == buyer and buyer != seller:
        transaction = Transactions(buyer=buyer, seller=seller, payment=credit_card, apartment=apartment)
        transaction.save()
        apartment.sellerID = buyer
        apartment.save()
        if not credit_card.save:
            credit_card.delete()
        return render(request, 'Transactions/make_transaction.html', {
            'buyer': buyer,
            'apartment': apartment,
            'seller': seller,
            'credit_card': credit_card.cardNumber[-4:],
        })
    return render(request, 'apartments/index.html')

def review(request, apartment_id, payment_id=None):
    if payment_id == None:
        payment_id=request.POST['CardSelect']

    buyer = auth.get_user(request)
    apartment = get_object_or_404(Apartments, pk=apartment_id)
    credit_card = get_object_or_404(CardDetails, pk=payment_id)
    return render(request, 'Transactions/review.html', {
        'buyer': buyer,
        'apartment': apartment,
        'payment': credit_card,
        'credit_card': credit_card.cardNumber[-4:],
    })
