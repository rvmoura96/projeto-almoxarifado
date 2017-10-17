from django.contrib import admin
from .models import Equipamento, Item, Notebook
# Register your models here.

admin.site.register(Equipamento)
admin.site.register(Notebook)
admin.site.register(Item)