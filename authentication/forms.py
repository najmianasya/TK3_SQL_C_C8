from django import forms
from .models import Panitia

class PanitiaRegistrasiForm(forms.ModelForm):
    class Meta:
        model = Panitia
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'address',
            'status',
        ]
        widgets = {
            'status': forms.RadioSelect(choices=STATUS_CHOICES),
        }