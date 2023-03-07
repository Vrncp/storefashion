from django.forms import ModelForm
from .models import Task,Product
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','important']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['nombre', 'description','departamento','active']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'departamento':forms.TextInput(attrs={'class':'form-control'}),
            'active':forms.CheckboxInput(attrs={'class':'form-check-input '})
        }