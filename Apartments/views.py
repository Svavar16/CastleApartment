from django.shortcuts import render, redirect, get_object_or_404
from Apartments.forms.apartments_form import ApartmentsCreateForm
from Apartments.models import ApartmentImage, Apartments


def index(request):
    return render(request, 'apartments/index.html')


def create_apartment(request):
    if request.method == 'POST':
        form = ApartmentsCreateForm(data=request.POST)
        if form.is_valid():
            apartment = form.save()
            apartment_image = ApartmentImage(image=request.POST['image'], apartment=apartment)
            apartment_image.save()
            return redirect('apartment-index')
    else:
        form = ApartmentsCreateForm()
    return render(request, 'apartments/create_apartment.html', {
        'form': form
    })

def delete_apartment(request, id):
    apartment = get_object_or_404(Apartments, pk=id)
    apartment.delete()
    return redirect('apartment-index')
