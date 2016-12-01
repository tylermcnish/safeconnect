# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-01 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0004_remove_house_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='stories',
            field=models.CharField(choices=[('One Story', 'One Story'), ('Two Stories', 'Two Stories'), ('Three Stories', 'Three Stories')], default='One Story', max_length=200),
        ),
        migrations.AlterField(
            model_name='house',
            name='insolation',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='house',
            name='monthly_electricity_usage',
            field=models.DecimalField(decimal_places=0, default=600, max_digits=5),
        ),
    ]