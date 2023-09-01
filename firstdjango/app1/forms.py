from django import forms
from django.forms.widgets import NumberInput
from django.db import models
from .models import Person

CHOICE_LIST = [
    ('python', 'Python'),
    ('java', 'Java')
]

class DemoForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100, required=False)
    email = forms.EmailField()
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    age = forms.IntegerField()
    programming = forms.ChoiceField(choices=CHOICE_LIST, widget=forms.RadioSelect)
    upload = forms.FileField()

class DbToForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        label = {'name': 'Enter your name'}
"""
    MultipleChoiceField
    FileField

    required, label, initial, help_text
"""