from django import forms
from .models import IndexCard

from .models import (
    IndexCard
    )

class IndexCardForm(forms.ModelForm):
    class Meta:
        model = IndexCard
        fields = [
            "code",
            "section",
            "venue",
            "professor"
        ]