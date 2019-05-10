from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from User.forms.create_card import CreateCardForm
from User.forms.create_user import CreateUserForm


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            user = User.objects.create_user(username=form.username,
                                            email=form.email,
                                            password=form.password)
            user.first_name = form.first_name
            user.last_name = form.last_name
            user.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': CreateUserForm()
    })


def addCard(request):
    if request.method == 'POST':
        form = CreateCardForm(data=request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            user = request.user
            card.owner = user
            if card.cardNumber.isdigit() and card.CVV.isdigit() and int(card.cardNumber) > 0 and int(card.CVV) > 0:
                card.save()
                return redirect(('apartment-index'))
            else:
                raise forms.ValidationError("Invalid input")
    return render(request, 'user/credit_card.html', {
        'form': CreateCardForm()
    })


def getUserProfile(request, id):
    return render(request, 'User/user_profile.html', {
        'user': get_object_or_404(User, pk=id)
    })


