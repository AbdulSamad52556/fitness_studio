from rest_framework import serializers
from .models import Booking
from classes.models import FitnessClass

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'fitness_class', 'client_name', 'client_email', 'booking_time']
        extra_kwargs = {
            'booking_time': {'read_only': True}
        }
    
    def validate(self, data):
        fitness_class = data['fitness_class']
        if fitness_class.available_slots <= 0:
            raise serializers.ValidationError("This class is fully booked")
        return data