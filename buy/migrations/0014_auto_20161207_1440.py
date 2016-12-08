# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-07 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0013_auto_20161207_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='max_roof_production',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='house',
            name='roof_area',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=9),
        ),
    ]
