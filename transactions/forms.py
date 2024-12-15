from django import forms
from .models import Transaction

class DepositeForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount'] 