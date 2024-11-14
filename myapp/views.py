from django.shortcuts import render
from .models import Booking


# Home
def index_page(request):
    """ Display the home page """
    return render(request, "index.html")

# About
def about_page(request):
    """ Display the about page """
    return render(request, "about.html")

# Chefs
def chefs_page(request):
    """ Display the chefs page """
    return render(request, "chefs.html")

# Event
def event_page(request):
    """ Display the event page """
    return render(request, "event.html")

# Contact
def contact_page(request):
    """ Display the contact page """
    return render(request, "contact.html")

# Gallery
def gallery_page(request):
    """ Display the gallery page """
    return render(request, "gallery.html")

# Menu
def menu_page(request):
    """ Display the menu page """
    return render(request, "menu.html")

# Booking
def booking_page(request):
    """ Display the booking page """
    return render(request, "booking.html")


# Retrieve all bookings
def retrieve_bookings(request):
    """ Retrieve/fetch all Bookings """
    #create a variable to store these bookings
    bookings = Booking.objects.all()
    context = {'bookings':bookings}
    return render(request, 'show_booking.html', context)

#Delete
def delete_booking(request, id):
    """ Deleting """
    booking = Booking.objects.get(id=id) #fetch the particular booking by id
    booking.delete()
    # return redirect(myapp:show_bookings)#just remain on the same page