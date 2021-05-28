import django_filters
from .models import *

class BedListFilter(django_filters.FilterSet):

    class Meta:
        model = BedList
        fields = ['patient_critical_level', 'Pincode', 'Hospital', 'Timeslot']