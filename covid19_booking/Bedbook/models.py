from django.db import models
from django.conf import settings
from django.utils import timezone
import os
# Create your models here.

class BedList(models.Model):
    PatientName = models.CharField(max_length=200)
    Contact_Number = models.CharField(max_length=15)
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    Gender = models.CharField(max_length=20, choices= GENDER_CHOICES, default='M')
    Patient_address = models.CharField(max_length=200)
    patient_critical_level = models.CharField(max_length=100)
    Pincode = models.CharField(max_length=6) 
    Hospital = models.CharField(max_length=200)
    Timeslot = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return self.PatientName