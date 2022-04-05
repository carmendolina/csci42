from django import forms
from .models import IndexCard
from django.forms import TextInput
from django.forms import Textarea

from .models import (
    IndexCard, ClassModel, ClassCode
    )

class CodeForm(forms.ModelForm):
    class Meta:
        model=ClassCode
        fields = [
            "name"
        ]
class LockedForm(forms.ModelForm):
    class Meta:
        model=ClassModel
        fields = [
            "islocked"
        ]

class CourseForm(forms.ModelForm):
    class Meta:
        model=ClassModel
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
                'class': "coursecode forminput",
                'placeholder': 'ex. CSCI 42'
            }),
            'section': TextInput(attrs={
                'class': "section forminput sectioninput",
                'placeholder': 'ex. B'
            }),
            'sched': TextInput(attrs={
                'class': "forminput sectioninput",
                'placeholder': 'ex. M-W-F; T-TH; SAT'
            }),
            'start': TextInput(attrs={
                'class': "timeinput forminput sectioninput",
                'placeholder': 'ex. 09:00'
            }),
            'end': TextInput(attrs={
                'class': "timeinput forminput sectioninput",
                'placeholder': 'ex. 13:30'
            }),
            'venue': TextInput(attrs={
                'class': "forminput sectioninput",
                'placeholder': 'ex. ONLINE'
            }),
            'professor': TextInput(attrs={
                'class': "forminput sectioninput",
                'placeholder': 'ex. JONGKO'
            })
        }

class ClassCopyPasteForm(forms.ModelForm):
    class Meta:
        model = ClassModel
        fields = [
            'copypaste'
        ]
        widgets = {
            'copypaste': Textarea(attrs={
                'class': "textarea",
                'placeholder': 'Paste from AISIS Class Schedule here...'
            }),
        }



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
                'class': "coursecode forminput",
                'placeholder': 'ex. CSCI 42'
            }),
            'section': TextInput(attrs={
                'class': "section forminput sectioninput",
                'placeholder': 'ex. B'
            }),
            'sched': TextInput(attrs={
                'class': "forminput sectioninput",
                'placeholder': 'ex. M-W-F; T-TH; SAT'
            }),
            'start': TextInput(attrs={
                'class': "timeinput forminput sectioninput",
                'placeholder': 'ex. 09:00'
            }),
            'end': TextInput(attrs={
                'class': "timeinput forminput sectioninput",
                'placeholder': 'ex. 13:30'
            }),
            'venue': TextInput(attrs={
                'class': "forminput sectioninput",
                'placeholder': 'ex. ONLINE'
            }),
            'professor': TextInput(attrs={
                'class': "forminput sectioninput",
                'placeholder': 'ex. JONGKO'
            })
        }

class CopyPasteForm(forms.ModelForm):
    class Meta:
        model = IndexCard
        fields = [
            'copypaste'
        ]
        widgets = {
            'copypaste': Textarea(attrs={
                'class': "textarea",
                'placeholder': 'Paste from AISIS Class Schedule here...'
            }),
        }