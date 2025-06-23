from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/')
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    coordinators = models.CharField(max_length=255, help_text="Comma-separated names")

    def __str__(self):
        return self.title


class UserMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject

class SignupData(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)  
    
    def __str__(self):
        return self.full_name


class LoginRecord(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.email} at {self.timestamp}"
    
    
class EventBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.title} on {self.booking_date}"
   
class UserSuggestion(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"
    


class BeachWeddingBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    package = models.CharField(max_length=100)
    special_requests = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

