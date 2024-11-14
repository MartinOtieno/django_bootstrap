from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)  # Name of the person making the reservation
    email = models.EmailField(max_length=254)  # Email address of the person
    phone = models.CharField(max_length=20)  # Phone number of the person
    date = models.DateField()  # Reservation date
    time = models.TimeField()  # Reservation time
    people = models.PositiveIntegerField()  # Number of people for the reservation
    message = models.TextField(blank=True)  # Additional message from the user (optional)
    
    def __str__(self):
        return self.name
