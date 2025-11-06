from django.forms import ModelForm
from .models import Cultivo

class CultivoForm(ModelForm):
    class Meta:
        model = Cultivo
        fields = ['nombreCultivo', 'description', 'typeCultivo']