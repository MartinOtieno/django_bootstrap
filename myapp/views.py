from django.shortcuts import render, redirect, get_object_or_404
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
    
    #update
    # def update_booking(request, booking_id):
    #     """ update the booking """
    #     booking = get_object_or_404(Booking, id=booking_id)
        #Put the condition for the form to update
        # if request.method == 'POST':
        #     booking.name = request.POST.get('name'),
        #     booking.email = request.POST.get('email'),
        #     booking.phone = request.POST.get('phone'),
        #     booking.date = request.POST.get('date'),
        #     booking.time = request.POST.get('time'),
        #     booking.people = request.POST.get('people'),
        #     booking.message = request.POST.get('message'),
            #Once you click on the update button
            # booking.save()
            
            # return redirect("myapp:show_bookings")
        # context('booking', booking)
        
        # return render(request, "update_booking.html")