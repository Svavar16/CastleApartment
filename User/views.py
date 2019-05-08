from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
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