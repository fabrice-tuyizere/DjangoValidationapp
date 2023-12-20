# models.py
import phonenumbers
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField
class Participants(models.Model):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    phone = PhoneNumberField(max_length=20)
    date_of_birth = models.DateField()
    reference_number = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    


class Vehicle(models.Model):
    Owner = models.ForeignKey(Participants, on_delete=models.CASCADE, related_name='vehicles')
    plate_number = models.CharField(max_length=20, unique=True,
     )
    color = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    manufacturer_date = models.DateField()

from django.contrib.auth.models import User
from django.db import models

class UserActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    