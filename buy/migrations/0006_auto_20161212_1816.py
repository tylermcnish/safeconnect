# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-13 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0005_auto_20161212_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliance_installer_availability',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy.Appliance_Installer'),
        ),
        migrations.AlterField(
            model_name='roof_installer_availability',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy.Roof_Installer'),
        ),
    ]