from django.contrib import admin
from .models import BedList

# Register your models here.
@admin.register(BedList)
class BedListAdmin(admin.ModelAdmin):
 list_display =['id', 'PatientName', 'Contact_Number', 'Gender', 'Patient_address', 'patient_critical_level', 'Pincode', 'Hospital', 'Timeslot']
 ordering=['id']