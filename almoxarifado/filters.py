from .models import Equipamento, Item
import django_filters

class EquipFilter(django_filters.FilterSet):
    class Meta:
        model = Equipamento
        fields = ['modelo', 'fabricante', 'status', 'tipo', 'ativo_imobilizado', ]

class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['item', 'tipo', 'status', ]