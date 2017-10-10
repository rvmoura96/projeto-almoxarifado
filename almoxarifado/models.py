from django.db import models
from django.utils import timezone

# Create your models here.
class Equipamento(models.Model):
    disponivel = 'Disponivel'
    indisponivel = 'Indisponivel'
    notebook = 'Notebook'
    desktop = 'Desktop'
    projetor = 'Projetor'
    impressora = 'Impressora'
    monitor = 'Monitor'

    tipo_choices = (
        (notebook, 'Notebook'),
        (desktop, 'Desktop'),
        (projetor, 'Projetor'),
        (impressora, 'Impressora'),
        (monitor, 'Monitor'),

    )

    status_choices = (
        (disponivel, 'Disponível'),
        (indisponivel, 'Indisponível'),
    )

    tipo = models.CharField(max_length=50, choices=tipo_choices, default=notebook)
    modelo = models.CharField(max_length=170)
    fabricante = models.CharField(max_length=90, default= None)
    ativo_imobilizado = models.PositiveIntegerField(default=0, unique=True)
    serial_number = models.CharField(max_length=30, unique=True, default= None)
    status = models.CharField(max_length=12, choices=status_choices, default=disponivel)
    prateleira = models.PositiveIntegerField(default=0)
    observacoes = models.TextField(null=True, blank=True)
    cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.modelo

class Item(models.Model):
    disponivel = 'Disponivel'
    indisponivel = 'Indisponivel'

    perifericos = 'Periféricos'
    consumiveis = 'Consumíveis'

    status_choices = (
        (disponivel,' Disponível'),
        (indisponivel, 'Indisponível'),
    )

    tipo_choices = {
        (consumiveis, 'Consumíveis'),
        (perifericos, 'Periféricos'),
    }

    tipo = models.CharField(max_length=12, choices=tipo_choices, default=consumiveis)
    item = models.CharField(max_length=170)
    fabricante = models.CharField(max_length=90, default= None)
    quantidade = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=12, choices=status_choices, default=disponivel)
    prateleira = models.PositiveIntegerField(default=0)
    cadastro = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.item

