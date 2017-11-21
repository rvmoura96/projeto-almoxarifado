from .models import Equipamento, Item, Fabricante, TipoItens, Tipo, Modelo
import django_filters

class EquipFilter(django_filters.FilterSet):
    ativo_imobilizado = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Equipamento
        fields = ['modelo', 'fabricante', 'status', 'tipo', 'ativo_imobilizado', ]

class ItemFilter(django_filters.FilterSet):
    item = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Item
        fields = ['item', 'tipo', 'status', ]

class FabFilter(django_filters.FilterSet):
    fabricante = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Fabricante
        fields = ['fabricante', ]

class TipoItemFilter(django_filters.FilterSet):
    tipo = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = TipoItens
        fields = ['tipo', ]

class TipoFilter(django_filters.FilterSet):
    tipo = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Tipo
        fields = ['tipo', ]

class ModeloFilter(django_filters.FilterSet):
    modelo = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Modelo
        fields = ['modelo', ]