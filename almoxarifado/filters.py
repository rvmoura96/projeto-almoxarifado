from .models import Equipamento, Item, Fabricante
import django_filters

class EquipFilter(django_filters.FilterSet):
    class Meta:
        model = Equipamento
        fields = ['modelo', 'fabricante', 'status', 'tipo', 'ativo_imobilizado', ]

class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['item', 'tipo', 'status', ]

class FabFilter(django_filters.FilterSet):
    class Meta:
        model = Fabricante
        fields = ['fabricante', ]