from django.contrib import admin
from .models import Equipamento, Item, Tipo, TipoItens, Modelo, Fabricante
# Register your models here.

admin.site.register(Tipo)
admin.site.register(TipoItens)
admin.site.register(Modelo)
admin.site.register(Fabricante)
admin.site.register(Equipamento)
admin.site.register(Item)