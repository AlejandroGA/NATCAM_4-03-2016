# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-19 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_gatossucursal_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatossucursal',
            name='telefono',
            field=models.PositiveIntegerField(default=12121212),
            preserve_default=False,
        ),
    ]
