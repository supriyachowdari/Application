from django import forms
from .models import BookingModel

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = ['name', 'email', 'guests', 'time']
        widgets = {
            'time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
