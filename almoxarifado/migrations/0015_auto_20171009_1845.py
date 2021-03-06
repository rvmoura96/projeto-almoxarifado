# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0014_auto_20171009_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='ativo_imobilizado',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='prateleira',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='prateleira',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
