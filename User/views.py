from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from User.forms.create_card import CreateCardForm
from User.forms.create_user import CreateUserForm
from User.forms.select_card import SelectCardForm
from User.models import ProfileImage
from User.forms.edit_profile import EditProfileForm, EditImageForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)
        if form.is_valid() and len(request.POST['image']) < 1000:
            form = form.save(commit=False)
            user = User.objects.create_user(username=form.username,
                                            email=form.email,
                                            password=form.password)
            user.first_name = form.first_name
            user.last_name = form.last_name
            if request.POST['image']:
                userImage = ProfileImage(img=request.POST['image'], user=user)
            else:
                userImage = ProfileImage(img='', user=user)
            user.save()
            userImage.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': CreateUserForm()
    })


@login_required
def editProfile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile', id=user.id)
    return render(request, 'user/edit_profile.html', {
        'form': EditProfileForm(instance=user)
    })


@login_required()
def editImage(request):
    user = request.user
    image = ProfileImage.objects.filter(user=user)
    if request.method == 'POST':
        form = EditImageForm(instance=image.first(), data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile', id=user.id)
    return render(request, 'user/change_image.html', {
        'form': EditImageForm(instance=image.first())
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


def getUserProfile(request, id=None):
    if not id:
        user = request.user
        if user.is_authenticated:
            return render(request, 'User/user_profile.html', {
                'profile_user': user
            })
    return render(request, 'User/user_profile.html', {
        'profile_user': get_object_or_404(User, pk=id)
    })


@login_required()
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('myprofile')
    return render(request, 'User/change_password.html', {
        'form': PasswordChangeForm(user)
    })

