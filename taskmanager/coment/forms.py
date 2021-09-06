from django.forms import ModelForm,TextInput
from .models import *

class COMENTForm(ModelForm):
    class Meta:
        model = Coment
        fields = ['title','number','task']

        widgets = {

            'title' : TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Атыңызды жазыңыз'
            }),

            'number' : TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Номеріңізді енгізіңіз'
            }),

            'task' : TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Сұрағыңызды қойыңыз....'
            })

        }