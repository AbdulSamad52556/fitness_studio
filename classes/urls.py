from django.urls import path
from .views import FitnessClassListView

urlpatterns = [
    path('', FitnessClassListView.as_view(), name='class-list'),
]