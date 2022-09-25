from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

from .models import *

#Here you can create your forms

class SubjectForm(forms.ModelForm):
    name = models

    class Meta:
        model = Subject
        fields = ('name', 'teacher')

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'teacher' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

class HomeworkForm(forms.ModelForm):
    name = models
    

    class Meta:
        model = Homework
        fields = ('title', 'subject', 'description')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'subject' : forms.Select(attrs={'class' : 'form-select'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control'}),
            
        }

