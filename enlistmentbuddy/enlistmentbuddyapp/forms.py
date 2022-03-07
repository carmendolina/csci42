from django import forms

class IndexCardForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=100)
    section = forms.CharField(label='CSCI40 Section', max_length=5)
    age = forms.IntegerField(label='Current Age')