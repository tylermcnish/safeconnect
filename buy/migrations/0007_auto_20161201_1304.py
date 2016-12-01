# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-01 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0006_house_your_current_electricity_provider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='main_service_capacity',
        ),
        migrations.AddField(
            model_name='house',
            name='busbar_capacity',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='house',
            name='is_there_room_for_new_breaker_opposite_main_breaker',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Help me figure it out', 'Help me figure it out')], default='Yes', max_length=200),
        ),
        migrations.AddField(
            model_name='house',
            name='main_breaker_size',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='house',
            name='roof_area',
            field=models.DecimalField(decimal_places=2, default=3000, max_digits=5),
        ),
    ]
