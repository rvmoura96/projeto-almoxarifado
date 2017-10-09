from django import forms
from .models import Equipamento

class EquipForm(forms.ModelForm):
    
    class Meta:
        model = Equipamento
        fields = ('tipo', 'modelo', 'fabricante', 'ativo_imobilizado',
                  'serial_number', 'status', 'prateleira', 'observacoes')