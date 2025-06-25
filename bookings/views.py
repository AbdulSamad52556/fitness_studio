from rest_framework import generics, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from classes.models import FitnessClass

class CreateBookingView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        fitness_class = serializer.validated_data['fitness_class']
        fitness_class.available_slots -= 1
        fitness_class.save()
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ClientBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    
    def get_queryset(self):
        email = self.request.query_params.get('email')
        if not email:
            return Booking.objects.none()
        return Booking.objects.filter(client_email=email)