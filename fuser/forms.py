from django import forms
from django.forms import ModelForm
from django.forms import fields, widgets
from .models import MovementPass


class PassApplyForm(ModelForm):
    
    class Meta:
        model = MovementPass
        fields = ['from_m','to_m',
                'district',
                'sub_dristrict',
                'reason',
                'move',
                'date',
                'time_spand'
        ]
        widgets ={
            'from_m':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Location'}),
            'to_m':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Location'}),
            'district':forms.Select(attrs={'class':'form-control','placeholder':'Enter Your District Name',}),
            'sub_dristrict':forms.TextInput(attrs={'class':'form-control','placeholder':'Subdistrict Name'}),
            'date':forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local'}),
            'time_spand':forms.Select(attrs={'class':'form-control'}),
            'move':forms.Select(attrs={'class':'form-control'}),
            'reason':forms.Select(attrs={'class':'form-control'})

        }
