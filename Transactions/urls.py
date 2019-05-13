from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('finalize/<int:apartment_id>/<int:payment_id>', views.make_transaction, name='make_transaction'),
    path('review/<int:apartment_id>/<int:payment_id>', views.review, name='review'),
    path('review/<int:apartment_id>', views.review, name='review_select'),
]