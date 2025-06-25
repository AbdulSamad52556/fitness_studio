from rest_framework import serializers
from .models import FitnessClass

class FitnessClassSerializer(serializers.ModelSerializer):
    local_datetime = serializers.SerializerMethodField()
    timezone = serializers.CharField(write_only=True, required=False, default='Asia/Kolkata')
    
    class Meta:
        model = FitnessClass
        fields = ['id', 'name', 'datetime', 'local_datetime', 'instructor', 
                 'max_slots', 'available_slots', 'timezone']
        read_only_fields = ['available_slots']
    
    def get_local_datetime(self, obj):
        request = self.context.get('request')
        tz = request.query_params.get('timezone', 'Asia/Kolkata') if request else 'Asia/Kolkata'
        return obj.local_datetime(tz)