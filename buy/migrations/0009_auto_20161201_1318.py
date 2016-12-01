# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-01 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0008_auto_20161201_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='busbar_capacity',
            field=models.DecimalField(decimal_places=0, default=100, max_digits=5),
        ),
        migrations.AlterField(
            model_name='house',
            name='main_breaker_size',
            field=models.DecimalField(decimal_places=0, default=100, max_digits=5),
        ),
    ]
