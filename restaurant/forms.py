from django import forms
from .models import BookingModel
from .models import Payment

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = ['name', 'email', 'guests', 'time']
        widgets = {
            'time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [ 'amount', 'payment_method']