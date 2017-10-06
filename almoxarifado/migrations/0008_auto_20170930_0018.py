# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0007_auto_20170929_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='ativo_imobilizado',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='status',
            field=models.CharField(choices=[('Disponivel', 'Disponivel'), ('Indisponivel', 'Indisponivel')], default='Disponivel', max_length=12),
        ),
    ]
