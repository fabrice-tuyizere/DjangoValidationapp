# forms.py
import re
from datetime import date
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django import forms
from .models import Participants,Vehicle
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


UR_AC_RW_EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@ur\.ac\.rw$')

def validate_ur_ac_rw_email(value):
    if not UR_AC_RW_EMAIL_PATTERN.match(value):
        raise ValidationError('Email must be in the format username@ur.ac.rw.')


class PersonForm(forms.ModelForm):
    class Meta:
        model = Participants
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'reference_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number between 99 and 999'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your UR email (Hint: username@ur.ac.rw)'}),
            'phone': PhoneNumberPrefixWidget(attrs={'class': 'form-control'}),
        }
     
    email = forms.EmailField(validators=[validate_ur_ac_rw_email])
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control'}))
    reference_number = forms.IntegerField(
    widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number between 99 and 999'}),
)
 
    
    
    def clean_reference_number(self):
        reference_number = self.cleaned_data['reference_number']
        if not 99 <= reference_number <= 999:
            raise forms.ValidationError("Reference number must be between 99 and 999.")
        return reference_number    

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']

        # Calculate age based on the current date
        age = (date.today() - date_of_birth).days // 365

        # Validate that the person is at least 18 years old
        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old.")

        return date_of_birth



class VehicleForm(forms.ModelForm):

     # Custom validator for plate_number
    validate_plate_number = RegexValidator(
        regex=r'^(RA[ABCDEFGH]|RNP|RDF|GR|IT)\d{3}[A-Za-z]$',
        message='Invalid plate number format. Please use the format RA###X, RNP###X, RDF###X, GR###X, or IT###X'
    )

    plate_number = forms.CharField(
        max_length=20,
        validators=[validate_plate_number],
        # widget=forms.TextInput(attrs={'class': 'form-control'})
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Format RA###X, RNP###X, RDF###X, GR###X, or IT###X (e.g., RA123C)'}),

    )
    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {
            'manufacturer_date': forms.DateInput(attrs={'type': 'date'}),
        }

     

    def clean_manufacturer_date(self):
        manufacturer_date = self.cleaned_data.get('manufacturer_date')

        # Custom validation for manufacturer date
        if manufacturer_date and manufacturer_date.year < 2000:
            raise ValidationError('Cars manufactured before 2000 are not allowed.')

        return manufacturer_date     





def trigger_error(request):
    # Intentional error to test logging
    raise Exception("This is a test error.")        