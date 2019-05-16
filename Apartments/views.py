
import json
import random
import operator
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from Apartments.forms.apartments_form import ApartmentsCreateForm, LocationCreateForm
from Apartments.models import ApartmentImage, Apartments, SearchHistory
from django.http import JsonResponse, HttpResponse
from Apartments.forms.change_price_form import ChangePriceForm


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        apartments = [{
            'id': x.id,
            'price': x.price,
            'size': x.size,
            'locationID': x.locationID.id,
            'locationID_streetName': x.locationID.streetName,
            'locationID_houseNumber': x.locationID.houseNumber,
            'yearBuild': x.yearBuild,
            'description': x.description,
            'firstImage': x.apartmentimage_set.first().image,
        } for x in Apartments.objects.filter(locationID__streetName__icontains=search_filter, forSale=True)]
        if 'search_filter' in request.GET and request.user.is_authenticated:
            search_filter = request.GET['search_filter']
            streetName = "Street name: "
            user = request.user
            searchedObject = SearchHistory.objects.create(userID=user, searchItem=streetName + search_filter)
            searchedObject.save()
        return JsonResponse({'data': apartments})
    context = {'apartments': Apartments.objects.all().filter(forSale=True)}
    return render(request, 'apartments/index.html', context)


def all_listing(request):
    def return_Json_responce(data):
        apartments = [{
            'id': x.id,
            'price': x.price,
            'size': x.size,
            'locationID': x.locationID.id,
            'locationID_streetName': x.locationID.streetName,
            'locationID_houseNumber': x.locationID.houseNumber,
            'yearBuild': x.yearBuild,
            'description': x.description,
            'firstImage': x.apartmentimage_set.first().image,
        } for x in data]
        return JsonResponse({'data': apartments})

    # get the Json if they are searching by price
    if 'arrange_by_price_asc' in request.GET:
        arrange_by_price_asc = Apartments.objects.all().order_by('-price').filter(forSale=True)
        return return_Json_responce(arrange_by_price_asc)

    # get the Json if they are searching by price
    if 'arrange_by_price_desc' in request.GET:
        arrange_by_price_desc = Apartments.objects.all().order_by('price').filter(forSale=True)
        return return_Json_responce(arrange_by_price_desc)

    #get the Json if they are searching for a name
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        search_filter_list = Apartments.objects.filter(locationID__streetName__icontains=search_filter, forSale=True)
        if 'search_filter' in request.GET and request.user.is_authenticated:
            search_filter = request.GET['search_filter']
            streetName = "Street name: "
            user = request.user
            searchedObject = SearchHistory.objects.create(userID=user, searchItem=streetName + search_filter)
            searchedObject.save()
        return return_Json_responce(search_filter_list)

    # get the Json, if they search by name asc
    if 'sort_name_asc' in request.GET:
        sort_name_asc = Apartments.objects.all().order_by('-locationID__streetName').filter(forSale=True)
        return return_Json_responce(sort_name_asc)

    # get the Json, if they search by name asc
    if 'sort_name_desc' in request.GET:
        sort_name_desc = Apartments.objects.all().order_by('locationID__streetName').filter(forSale=True)
        return return_Json_responce(sort_name_desc)

    #get the Json, to filter by postalCode
    if 'search_postal' in request.GET:
        search_postal = request.GET['search_postal']
        search_postal_list = Apartments.objects.filter(locationID__postalCode__exact=search_postal, forSale=True)
        if 'search_postal' in request.GET and request.user.is_authenticated:
            search_postal = request.GET['search_postal']
            postal_code = "Postal code: "
            userID = request.user
            searchedObject = SearchHistory.objects.create(userID=userID, searchItem=postal_code + search_postal)
            searchedObject.save()
        return return_Json_responce(search_postal_list)

    context = {'apartments': Apartments.objects.all().filter(forSale=True)}
    return render(request, 'apartments/all_listing.html', context)

def get_apartment_by_id(request, id):
    return render(request, 'apartments/single_apartment.html', {
        'apartments': get_object_or_404(Apartments, pk=id)
    })

@login_required
def create_apartment(request):
    if request.method == 'POST':
        apartment_form = ApartmentsCreateForm(data=request.POST)
        location_form = LocationCreateForm(data=request.POST)
        if all([apartment_form.is_valid(), location_form.is_valid()]):
            location = location_form.save()
            apartment = apartment_form.save(commit=False)
            apartment.locationID = location
            apartment.forSale = True
            apartment.sellerID = request.user
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

@login_required
def delete_apartment(request, id):
    apartment = get_object_or_404(Apartments, pk=id)
    apartment.delete()
    return redirect('apartment-index')


@permission_required('Apartments.change_apartments')
def change_price(request, id):
    if request.method == 'POST':
        price_form = ChangePriceForm(data=request.POST)
        if price_form.is_valid():
            apartment = get_object_or_404(Apartments, pk=id)
            apartment.price = request.POST['price']
            apartment.save()
        return redirect('apartment-index')
    context = {
        'form': ChangePriceForm,
        'id': id
    }
    return render(request, 'apartments/change_price.html', context)


def get_three_random_apartments(request):
    apartmentsList = Apartments.objects.all().filter(forSale=True)
    apartments = []
    for apartment in apartmentsList:
        apartments.append({"id": apartment.id,
                           "description": apartment.description,
                           "locationID_streetname": apartment.locationID.streetName,
                           "locationID_houseNum": apartment.locationID.houseNumber,
                           "first_image": apartment.apartmentimage_set.first().image})
    retval = random.sample(apartments, 3)
    return JsonResponse(retval, safe=False)


def get_newest_apartment(request):
    apartment_list = Apartments.objects.all().filter(forSale=True)
    apartment_new = sorted(apartment_list, key=operator.attrgetter('id'))[::-1][0]

    apartment_image = []
    apartment_image.append({"image": apartment_new.apartmentimage_set.first().image,
                            "id": apartment_new.id,
                            "locationID_streetname": apartment_new.locationID.streetName,
                            "locationID_houseNum": apartment_new.locationID.houseNumber})

    return JsonResponse(apartment_image, safe=False)


