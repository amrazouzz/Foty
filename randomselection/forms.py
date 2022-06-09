from cProfile import label
from dataclasses import field
from tkinter import Widget
from xml.dom.minidom import Attr
from django import forms
from django.forms import ModelForm
from .models import Selection, Player, Team

class SelectionForm(ModelForm):
    class Meta:
        model = Selection
        fields = ('name',)
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control text-center','placeholder':'مثال: ماتش الخميس'}),
        }
        labels = {
            'name':'اسم التقسيمة',
        }

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ('name','position','number',)
        labels = {
            'name':'اسم اللاعب',
            'position':'مركز اللاعب',
            'number':'رقم اللاعب',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control text-center', 'placeholder':'اسم اللاعب'}),
            'position':forms.Select(choices=model.POSITION, attrs={'class':'form-control text-center'}),
            'number':forms.Select(choices=model.NUMBERS,attrs={'class':'form-control text-center'}),
        }
        
