from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'apartments/index.html')


def create_apartment(request):
    if request.method == 'POST':
        print(1)
    else:
        print(2)
    return render(request, 'apartments/create_apartment.html', {
        'form': form
    })
