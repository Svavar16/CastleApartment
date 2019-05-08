from django.shortcuts import render, redirect, get_object_or_404
from Apartments.forms.apartments_form import ApartmentsCreateForm, LocationCreateForm
from Apartments.models import ApartmentImage, Apartments, Location


def index(request):
    return render(request, 'apartments/index.html')


def apartment_details(request, id):
    render(request, 'apartments/apartment_details.html', {
        'apartment': get_object_or_404(Apartments, pk=id)
    })


def create_apartment(request):
    if request.method == 'POST':
        apartment_form = ApartmentsCreateForm(data=request.POST)
        if apartment_form.is_valid():
            apartment = apartment_form.save()
            apartment_image = ApartmentImage(candyImage=request.POST['image'], apartmentID=apartment)
            apartment_image.save()
            return redirect('apartment-index')
    else:
        apartment_form = ApartmentsCreateForm()
    return render(request, 'apartments/create_apartment.html', {
        'apartment_form': apartment_form,
    })


def delete_apartment(request, id):
    apartment = get_object_or_404(Apartments, pk=id)
    apartment.delete()
    return redirect('apartment-index')


def create_location(request):
    if request == 'POST':
        location_form = LocationCreateForm(data=request.POST)
        if location_form.is_valid():
            location = location_form.save()
            location.save()
            return redirect('create_apartment')
    else:
        form = LocationCreateForm()
    return render(request, 'apartments/create_location.html', {
        'form': form
    })