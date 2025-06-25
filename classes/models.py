from django.db import models
from django.utils import timezone
import pytz

class FitnessClass(models.Model):
    CLASS_TYPES = [
        ('YOGA', 'Yoga'),
        ('ZUMBA', 'Zumba'),
        ('HIIT', 'HIIT'),
    ]
    
    name = models.CharField(max_length=50, choices=CLASS_TYPES)
    datetime = models.DateTimeField()  # Stored in UTC
    instructor = models.CharField(max_length=100)
    max_slots = models.PositiveIntegerField()
    available_slots = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.get_name_display()} with {self.instructor} at {self.local_datetime()}"
    
    def local_datetime(self, tz='Asia/Kolkata'):
        """Convert UTC time to local timezone"""
        return timezone.localtime(self.datetime, timezone=pytz.timezone(tz))
    
    def save(self, *args, **kwargs):
        """Set available_slots to max_slots if not set"""
        if not self.available_slots:
            self.available_slots = self.max_slots
        super().save(*args, **kwargs)