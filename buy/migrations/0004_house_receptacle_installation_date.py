# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-11 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0003_house_receptacle_installer'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='receptacle_installation_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
