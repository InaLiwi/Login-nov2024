from django import forms

from .models import login

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__'
        widgets = {
            'usuario_nombre': forms.TextInput(attrs={'type': 'text'}),
            'usuario_password': forms.TextInput(attrs={'type': 'text'}), 
        }