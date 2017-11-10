from .models import Equipamento
import django_filters

class EquipFilter(django_filters.FilterSet):
    class Meta:
        model = Equipamento
        fields = ['modelo', 'fabricante', 'status', 'tipo', ]