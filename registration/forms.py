from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['grade', 'name', 'unit', 'email', 'will_attend']