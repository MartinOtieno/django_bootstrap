from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField()
    message = models.TextField()
    
    #to return the values in the human readable format
    def __str__(self):
        return self.name
    
    from django.db import models

class UploadedImage(models.Model):
    title = models.CharField(max_length=108)  # A text field for the title
    image = models.ImageField(upload_to='uploaded_images/')  # Directory for image uploads

    def __str__(self):
        return self.title  # String representation

