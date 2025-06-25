from django.core.management.base import BaseCommand
from classes.models import FitnessClass
from django.utils import timezone
import pytz

class Command(BaseCommand):
    help = 'Seed initial fitness classes'
    
    def handle(self, *args, **options):
        ist = pytz.timezone('Asia/Kolkata')
        
        classes = [
            {
                'name': 'YOGA',
                'datetime': ist.localize(timezone.datetime(2025, 12, 25, 9, 0)),
                'instructor': 'Instructor1',
                'max_slots': 15
            },
            {
                'name': 'ZUMBA',
                'datetime': ist.localize(timezone.datetime(2025, 12, 26, 18, 0)),
                'instructor': 'Instructor2',
                'max_slots': 20
            },
            {
                'name': 'HIIT',
                'datetime': ist.localize(timezone.datetime(2025, 12, 27, 10, 0)),
                'instructor': 'Instructor3',
                'max_slots': 24
            }
        ]
        
        for class_data in classes:
            FitnessClass.objects.create(**class_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded classes'))