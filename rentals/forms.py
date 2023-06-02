from django import forms
from .models import CarRental

class BookingForm(forms.ModelForm):
    class Meta:
        model= CarRental
        fields = ['car','customer','start_date','end_date',]
        widgets = {
            'car': forms.Select(attrs={'class': 'form-control'}),
            'customer':forms.Select(attrs={'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
        }