# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-19 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20160318_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatossucursal',
            name='agua',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='gatossucursal',
            name='luz',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
