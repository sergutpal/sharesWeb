# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-20 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharesWebApp', '0045_auto_20170430_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='description',
            field=models.CharField(blank=True, max_length=8000, null=True, verbose_name='Notas'),
        ),
    ]
