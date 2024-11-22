from django import forms
from .models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'description', 'image']  # Updated for renamed field
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
