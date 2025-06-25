from rest_framework import generics
from .models import FitnessClass
from .serializers import FitnessClassSerializer
from django.utils import timezone

class FitnessClassListView(generics.ListAPIView):
    serializer_class = FitnessClassSerializer
    queryset = FitnessClass.objects.filter(datetime__gte=timezone.now())
    
    def get_serializer_context(self):
        return {'request': self.request}