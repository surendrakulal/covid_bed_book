# Generated by Django 3.0.5 on 2021-05-28 10:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BedList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientName', models.CharField(max_length=200)),
                ('Contact_Number', models.CharField(max_length=15)),
                ('Gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=20)),
                ('Patient_address', models.CharField(max_length=200)),
                ('patient_critical_level', models.CharField(max_length=100)),
                ('Pincode', models.CharField(max_length=6)),
                ('Hospital', models.CharField(max_length=200)),
                ('Timeslot', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]