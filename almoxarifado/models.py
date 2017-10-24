from django.db import models
from django.utils import timezone

# Create your models here.

class Tipo(models.Model):
    tipo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo

class TipoItens(models.Model):
    tipo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo

class Modelo(models.Model):
    modelo = models.CharField(max_length=170, unique=True)

    def __str__(self):
        return self.modelo

class Fabricante(models.Model):
    fabricante = models.CharField(max_length=90, unique=True)

    def __str__(self):
        return self.fabricante

class Equipamento(models.Model):
    
    disponivel = 'Disponivel'
    indisponivel = 'Indisponivel'

    status_choices = (
        (disponivel, 'Disponível'),
        (indisponivel, 'Indisponível'),
    )

    tipo = models.ForeignKey(Tipo)
    modelo = models.ForeignKey(Modelo)
    fabricante = models.ForeignKey(Fabricante)
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

    status_choices = (
        (disponivel,' Disponível'),
        (indisponivel, 'Indisponível'),
    )

    tipo = models.ForeignKey(TipoItens)
    item = models.CharField(max_length=170)
    fabricante = models.ForeignKey(Fabricante)
    quantidade = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=12, choices=status_choices, default=disponivel)
    prateleira = models.PositiveIntegerField(default=0)
    cadastro = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.item

