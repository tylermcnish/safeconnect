# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-12 23:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0004_house_receptacle_installation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_capacity', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('number_of_modules', models.IntegerField(default=0)),
                ('smartbox_size', models.IntegerField(default=0)),
                ('system_value', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('system_production', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('percent_of_electric_bill', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('receptacle_installation_date', models.DateField(blank=True, null=True)),
                ('roof_installation_date', models.DateField(blank=True, null=True)),
                ('appliance_installation_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appliance_Installer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('about', models.CharField(default='info about me here', max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, default=750, max_digits=9)),
                ('roof_installer_pic', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Appliance_Installer_Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_date', models.DateField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy.Receptacle_Installer')),
            ],
        ),
        migrations.CreateModel(
            name='Roof_Installer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('about', models.CharField(default='info about me here', max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, default=750, max_digits=9)),
                ('roof_installer_pic', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Roof_Installer_Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_date', models.DateField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy.Receptacle_Installer')),
            ],
        ),
        migrations.RemoveField(
            model_name='receptacle_installation',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='receptacle_installation',
            name='house',
        ),
        migrations.RemoveField(
            model_name='receptacle_installation',
            name='receptacle_installer',
        ),
        migrations.RemoveField(
            model_name='system',
            name='house',
        ),
        migrations.RemoveField(
            model_name='house',
            name='number_of_modules',
        ),
        migrations.RemoveField(
            model_name='house',
            name='percent_of_electric_bill',
        ),
        migrations.RemoveField(
            model_name='house',
            name='receptacle_installation_date',
        ),
        migrations.RemoveField(
            model_name='house',
            name='receptacle_installer',
        ),
        migrations.RemoveField(
            model_name='house',
            name='smartbox_size',
        ),
        migrations.RemoveField(
            model_name='house',
            name='system_capacity',
        ),
        migrations.RemoveField(
            model_name='house',
            name='system_production',
        ),
        migrations.RemoveField(
            model_name='house',
            name='system_value',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='receptacle_installation',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='system',
        ),
        migrations.DeleteModel(
            name='Receptacle_Installation',
        ),
        migrations.DeleteModel(
            name='System',
        ),
        migrations.AddField(
            model_name='appliance',
            name='appliance_installer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buy.Appliance_Installer'),
        ),
        migrations.AddField(
            model_name='appliance',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buy.House'),
        ),
        migrations.AddField(
            model_name='appliance',
            name='receptacle_installer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buy.Receptacle_Installer'),
        ),
        migrations.AddField(
            model_name='appliance',
            name='roof_installer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buy.Roof_Installer'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='appliance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='buy.Appliance'),
            preserve_default=False,
        ),
    ]
