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
    perifericos = 'Periféricos'
    consumiveis = 'Consumíveis'

    tipo_choices = (
        (notebook, 'Notebook'),
        (desktop, 'Desktop'),
        (projetor, 'Projetor'),
        (impressora, 'Impressora'),
        (monitor, 'Monitor'),
        (perifericos, 'Periféricos'),
        (consumiveis, 'Consumíveis'),

    )

    status_choices = (
        (disponivel, 'Disponivel'),
        (indisponivel, 'Indisponivel'),
    )

    tipo = models.CharField(max_length=50, choices=tipo_choices, default=notebook)
    modelo = models.CharField(max_length=170)
    fabricante = models.CharField(max_length=90, null=True, blank=True)
    ativo_imobilizado = models.IntegerField(null=True, blank=True)
    serial_number = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=12, choices=status_choices, default=disponivel)
    quantidade = models.PositiveIntegerField(default=1)
    data_retirada = models.DateField(null=True, blank=True)
    data_entrega  = models.DateField(null=True, blank=True)
    localizacao = models.CharField(max_length=150, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.modelo