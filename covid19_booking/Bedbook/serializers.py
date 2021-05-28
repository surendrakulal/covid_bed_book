from rest_framework import serializers
from .models import BedList

class BedListSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BedList
        fields = ['id', 'PatientName', 'Contact_Number', 'Gender', 'Patient_address', 'patient_critical_level', 'Pincode', 'Hospital', 'Timeslot']