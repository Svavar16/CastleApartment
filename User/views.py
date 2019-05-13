from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from User.forms.create_card import CreateCardForm
from User.forms.create_user import CreateUserForm
from User.forms.select_card import SelectCardForm
from User.models import ProfileImage


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
            if request.POST['image']:
                userImage = ProfileImage(img=request.POST['image'], user=user)
                userImage.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': CreateUserForm()
    })


def addCard(request, apartment_id):
    if request.method == 'POST':
        form = CreateCardForm(data=request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            user = request.user
            card.owner = user
            if card.cardNumber.isdigit() and card.CVV.isdigit() and int(card.cardNumber) > 0 and int(card.CVV) > 0:
                card.save()
                return redirect('review', apartment_id=apartment_id, payment_id=card.id)
            else:
                raise forms.ValidationError("Invalid input")
    return render(request, 'user/credit_card.html', {
        'createForm': CreateCardForm(),
        'selectForm': SelectCardForm(user=request.user),
        'apartment_id': apartment_id
    })


def getUserProfile(request, id):
    return render(request, 'User/user_profile.html', {
        'profile_user': get_object_or_404(User, pk=id)
    })


