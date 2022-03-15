from django import forms
from .models import IndexCard
from django.forms import TextInput

from .models import (
    IndexCard
    )

class IndexCardForm(forms.ModelForm):
    class Meta:
        model = IndexCard
        fields = [
            "code",
            "section",
            "sched",
            "start",
            "end",
            "venue",
            "professor"
        ]
        widgets = {
            'code': TextInput(attrs={
                'class': "coursecode",
                'placeholder': 'CSCI 42'
            }),
            'section': TextInput(attrs={
                'class': "section",
                'placeholder': 'B'
            }),
            'sched': TextInput(attrs={
                'class': "forminput",
                'placeholder': 'M-W-F, T-TH'
            }),
            'start': TextInput(attrs={
                'class': "forminput",
                'placeholder': '09:00, 14:00'
            }),
            'end': TextInput(attrs={
                'class': "forminput",
                'placeholder': '10:00, 13:30'
            }),
            'venue': TextInput(attrs={
                'class': "forminput",
                'placeholder': 'ONLINE'
            }),
            'professor': TextInput(attrs={
                'class': "forminput",
                'placeholder': 'JONGKO'
            })
        }