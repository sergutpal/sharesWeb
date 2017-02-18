# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sharesWebApp', '0004_alarm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarm',
            name='changePrice',
        ),
        migrations.AddField(
            model_name='alarm',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alarm',
            name='changePriceHigh',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='alarm',
            name='changePriceLow',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='alarm',
            name='maxPrice',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='currency',
            name='symbol',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='minPrice',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='share',
            name='ISIN',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='share',
            name='description',
            field=models.CharField(blank=True, max_length=8000, null=True),
        ),
        migrations.AlterField(
            model_name='share',
            name='index',
            field=models.ForeignKey(blank=True, db_column='idIndex', null=True, on_delete=django.db.models.deletion.CASCADE, to='sharesWebApp.Index'),
        ),
        migrations.AlterField(
            model_name='share',
            name='ticker',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sharefonds',
            name='maxPrice',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='sharefonds',
            name='minPrice',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
    ]
