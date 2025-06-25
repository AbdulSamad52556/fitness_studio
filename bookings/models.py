from django.db import models
from classes.models import FitnessClass

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booking_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.client_name} booked {self.fitness_class}"