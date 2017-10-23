from django import forms
from .models import Equipamento, Fabricante, Item, Tipo

class EquipForm(forms.ModelForm):
    
    class Meta:
        model = Equipamento
        fields = ('tipo', 'modelo', 'fabricante', 'ativo_imobilizado',
                  'serial_number', 'status', 'prateleira', 'observacoes', )

class FabricanteForm(forms.ModelForm):
    
    class Meta:
        model = Fabricante
        fields = ('fabricante',)

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('tipo', 'item', 'fabricante', 'quantidade',
                  'status', 'prateleira', )

class TipoEquipForm(forms.ModelForm):

    class Meta:
        model = Tipo
        fields = ('tipo', )