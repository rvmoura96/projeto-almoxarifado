# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0013_auto_20171009_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantidade',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='tipo',
            field=models.CharField(choices=[('Periféricos', 'Periféricos'), ('Consumíveis', 'Consumíveis')], default='Consumíveis', max_length=12),
        ),
    ]