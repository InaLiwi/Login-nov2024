from django import forms

from .models import Usuario

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'usuario_nombre': forms.TextInput(attrs={'type': 'text'}),
            'usuario_password': forms.TextInput(attrs={'type': 'text'}), 
        }