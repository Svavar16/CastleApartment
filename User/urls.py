from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name="login"),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('credit_card/<int:apartment_id>', views.addCard, name='credit_card'),
    path('profile/<int:id>', views.getUserProfile, name='user_profile'),
    path('profile', views.getUserProfile, name='myprofile'),
    path('edit_profile', views.editProfile, name='edit_profile'),
    path('change_image', views.editImage, name='change_image'),
    path('change_password', views.change_password, name='change_password'),
]