from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('<int:apartment_id>', views.make_transaction, name='make_transaction'),
]