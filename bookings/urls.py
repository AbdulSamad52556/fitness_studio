from django.urls import path
from .views import CreateBookingView, ClientBookingsView

urlpatterns = [
    path('book/', CreateBookingView.as_view(), name='create-booking'),
    path('', ClientBookingsView.as_view(), name='client-bookings'),
]