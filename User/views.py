from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from User.forms.create_user import CreateUserForm


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': CreateUserForm()
    })