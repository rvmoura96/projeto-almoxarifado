# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 23:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0024_auto_20171018_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='fabricante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almoxarifado.Fabricante'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almoxarifado.Modelo'),
        ),
    ]
