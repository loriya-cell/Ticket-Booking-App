# booking/models.py
from django.db import models
from django.contrib.auth.models import User

class Show(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats = models.IntegerField()  # Ensure that this field exists
    # Add any other fields you need

    def __str__(self):
        return f"Booking for {self.user} to {self.show} seats: {self.seats}"
