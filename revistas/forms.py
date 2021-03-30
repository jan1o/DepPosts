from django.forms import ModelForm
from .models import Revista

class RevistaForm(ModelForm):
    class Meta:
        model = Revista
        fields = ['nome']
