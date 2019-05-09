from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="apartment-index"),
    path('all_listing', views.all_listing, name="apartment_all_listing"),
    path('all_listing/listing_by_price', views.all_listing_by_price, name="apartment_all_listing_by_price"),
    path('all_listing/listing_by_name', views.all_listing_by_name, name="apartment_all_listing_by_name"),
    path('all_listing/<int:id>', views.get_apartment_by_id, name='apartment_details'),
    path('create_apartment', views.create_apartment, name='create_apartment'),
    path('delete_apartment/<int:id>', views.delete_apartment, name='delete_apartment'),
    path('<int:id>/change_price', views.change_price, name='change_price'),
]