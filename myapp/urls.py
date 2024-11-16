from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('about/', views.about_page, name='about_page'),
    path('menu/', views.menu_page, name='menu_page'),
    path('events/', views.event_page, name='event_page'),
    path('chefs/', views.chefs_page, name='chefs_page'),
    path('gallery/', views.gallery_page, name='gallery_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('booking/', views.booking_page, name='booking_page'), 
    path('show_bookings/', views.retrieve_bookings, name='booking'),
    path('delete/<int:id>', views.delete_booking, name="delete"),
    # path('update/<int:id>', views.update_booking, name="update_booking")
]
