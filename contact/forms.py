from django import forms
from .models import Letter

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = (
            'client_name',
            'client_email',
            'client_phone',
            'title',
            'letter_subject',
            'message',
        )
