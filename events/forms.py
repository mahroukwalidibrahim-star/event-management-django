from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organisateur']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-3'}),
            'heure': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control mb-3'}),
            'titre': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'capacite_max': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'lieu': forms.Select(attrs={'class': 'form-select mb-3'}),
        }