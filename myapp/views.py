from django.shortcuts import render, redirect, get_object_or_404
#import the model
from .models import Booking
# Import the login_required

from django.contrib.auth.decorators import login_required

# from .models import UploadedImage
from myapp.models import UploadedImage
from django.core.files.storage import FileSystemStorage


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


# @login_required(login_url='accounts:login')
def booking(request): #Function to push the booking to the db
    """ Function to push the booking to the db """
    if request.method == 'POST':  
        # Create a new Booking object and save it
        bookings = Booking(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            time = request.POST['time'],
            people = request.POST['people'],
            message = request.POST['message'],
        )
        bookings.save()
        # Redirect to the 'index_page' after successful form submission
        return redirect('index_page')  # Use URL pattern name, not file path
    else:
        return render(request, 'booking.html')

# Retrieve all bookings
def retrieve_bookings(request):
    """ Retrieve/fetch all Bookings """
    # create a variable to store these bookings
    bookings = Booking.objects.all()
    context = {'bookings':bookings}
    return render(request, 'show_booking.html', context)
#Delete
def delete_booking(request, id):
    """Delete a booking by ID and redirect to the bookings list."""
    booking = get_object_or_404(Booking, id=id)  # Use get_object_or_404 for better error handling
    booking.delete()  # Delete the booking
    return redirect("show_bookings")  # Redirect to the page that lists all bookings

#update
def update_booking(request, booking_id):
    """Update the booking."""
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        # Update booking fields with form data
        booking.name = request.POST.get('name')
        booking.email = request.POST.get('email')
        booking.phone = request.POST.get('phone')
        booking.date = request.POST.get('date')
        booking.time = request.POST.get('time')
        booking.people = request.POST.get('people')
        booking.message = request.POST.get('message')
        booking.save()  # Save the updated booking
        
        return redirect("show_bookings")  # Redirect to the bookings list page
    
    # Pass the booking object to the template
    context = {'booking': booking}
    return render(request, "update_booking.html", context)

def upload_image(request):
    if request.method == 'POST':
        # Retrieve data from the form
        title = request.POST['title']
        uploaded_file = request.FILES['image']
        
        # Save the file using filesystemStorage
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        
        # Save file information to the database
        image = UploadedImage.objects.create(title=title, image=filename)
        image.save()
        
        return render(request, 'upload_success.html', {'file_url':file_url})
    return render(request, "upload_image.html")

# Adding the mpesa function

