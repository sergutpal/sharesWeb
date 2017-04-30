# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharesWebApp', '0039_auto_20170430_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharefonds',
            name='avgPrice',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Precio Medio'),
        ),
        migrations.AddField(
            model_name='sharefonds',
            name='favourite',
            field=models.BooleanField(default=False, verbose_name='Favorito'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sharefonds',
            name='percent',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='% del fondo'),
        ),
    ]
