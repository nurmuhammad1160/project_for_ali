# forms.py
from django import forms
from .models import Spravka

class SpravkaForm(forms.ModelForm):
    class Meta:
        model = Spravka
        fields = '__all__'
