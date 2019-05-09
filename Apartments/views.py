from django.shortcuts import render, redirect, get_object_or_404
from Apartments.forms.apartments_form import ApartmentsCreateForm, LocationCreateForm
from Apartments.models import ApartmentImage, Apartments
from django.http import JsonResponse


def index(request):
    if 'apartment-card-details' in request.GET:
        apartments = [{
            'id': x.id,
            'price': x.price,
            'size': x.size,
            'locationID': x.locationID,
            'rooms': x.rooms,
            'privateEntrance': x.privateEntrance,
            'animalsAllowed': x.animalsAllowed,
            'garage': x.garage,
            'yearBuild': x.yearBuild,
            'sellerID': x.sellerID,
            'firstImage': x.apartmentimage_set.first().candyImage,
        } for x in Apartments.objects.all().order_by('-price')]
        return JsonResponse({'data': apartments})
    context = {'apartments': Apartments.objects.all()}
    return render(request, 'apartments/index.html', context)


def all_listing(request):
    context = {'apartments': Apartments.objects.all()}
    return render(request, 'apartments/all_listing.html', context)


def all_listing_by_price(request):
    context = {'apartments': Apartments.objects.all().order_by('-price')}
    return render(request, 'apartments/all_listing.html', context)


def all_listing_by_name(request):
    context = {'apartments': Apartments.objects.all().order_by('-price')}
    return render(request, 'apartments/all_listing.html', context)


def get_apartment_by_id(request, id):
    return render(request, 'apartments/single_apartment.html', {
        'apartments': get_object_or_404(Apartments, pk=id)
    })


def create_apartment(request):
    if request.method == 'POST':
        apartment_form = ApartmentsCreateForm(data=request.POST)
        location_form = LocationCreateForm(data=request.POST)
        if all([apartment_form.is_valid(), location_form.is_valid()]):
            location = location_form.save()
            apartment = apartment_form.save(commit=False)
            apartment.locationID = location
            location.save()
            apartment.save()
            apartment_image = ApartmentImage(image=request.POST['image'], apartmentID=apartment)
            apartment_image.save()
            return redirect('apartment-index')
    else:
        apartment_form = ApartmentsCreateForm()
        location_form = LocationCreateForm()
    return render(request, 'apartments/create_apartment.html', {
        'apartment_form': apartment_form,
        'location_form': location_form,
    })


def delete_apartment(request, id):
    apartment = get_object_or_404(Apartments, pk=id)
    apartment.delete()
    return redirect('apartment-index')
