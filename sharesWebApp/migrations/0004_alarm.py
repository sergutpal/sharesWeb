# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sharesWebApp', '0003_auto_20170214_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minPrice', models.DecimalField(decimal_places=4, max_digits=10)),
                ('changePrice', models.DecimalField(decimal_places=4, max_digits=10)),
                ('share', models.ForeignKey(db_column='idShare', on_delete=django.db.models.deletion.CASCADE, to='sharesWebApp.Share')),
            ],
            options={
                'ordering': ['share'],
                'db_table': 'Alarm',
            },
        ),
    ]
