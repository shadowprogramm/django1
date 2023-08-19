from django import forms
from django.forms.widgets import NumberInput
from django.db import models

CHOICE_LIST = [
    ('python', 'Python'),
    ('java', 'Java')
]

class DemoForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100, help_text='Your Name')
    email = forms.EmailField()
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    age = forms.IntegerField()
    programming = forms.ChoiceField(choices=CHOICE_LIST, widget=forms.RadioSelect)
    upload = forms.FileField(upload_to='uploads/')


class DbToForm(models.Model):
    first_name = models.CharField(max_length=20, default="Christson")
    tax_code = models.CharField(
        max_length=20,
        unique=True
    )
    semestre = models.CharField(
        max_length=20,
        choices=CHOICE_LIST
    )

"""
    MultipleChoiceField
    FileField

    required, label, initial, help_text
"""