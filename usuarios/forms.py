from django.forms import ModelForm
from .models import *

class usuario_form(ModelForm):
    class Meta:
        model = Usuario
        fields = ['user', 'nome', 'revista']
