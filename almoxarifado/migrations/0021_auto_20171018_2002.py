# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0020_auto_20171018_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tipo',
            field=models.CharField(choices=[('Periféricos', 'Periféricos'), ('Consumíveis', 'Consumíveis')], default='Consumíveis', max_length=12),
        ),
    ]
