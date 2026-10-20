"""Define URL patterns for the Kokoro restaurant booking website."""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from bookings import views as index_views


urlpatterns = [
    path('admin/', 
        admin.site.urls
    ),

    path('', 
        index_views.index, 
        name='index'
    ),
    
    path('sign_up/', 
        index_views.signup, 
        name='signup'
    ),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'profile/',
        index_views.profile,
        name='profile'
    ),
    path(
        "book/<int:booking_id>/edit/",
        index_views.edit_booking,
        name="edit_booking",
    ),
    path(
        "book/<int:booking_id>/cancel/",
        index_views.cancel_booking,
        name="cancel_booking",
    ),
    path(
        'book/', 
        index_views.create_booking, 
        name='booking_page'
    ),
    path(
        'menu/',
        index_views.menu,
        name='menu'
    ),
    path(
        'book/availability/',
        index_views.available_times,
        name='available_times',
    ),
]