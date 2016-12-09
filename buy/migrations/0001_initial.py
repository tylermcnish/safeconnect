# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-09 01:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('insolation', models.DecimalField(decimal_places=3, default=5, max_digits=6)),
                ('roof_area', models.DecimalField(decimal_places=2, default=100, max_digits=6)),
                ('max_roof_capacity', models.DecimalField(decimal_places=0, default=632, max_digits=6)),
                ('max_roof_production', models.DecimalField(decimal_places=0, default=632, max_digits=6)),
                ('monthly_electricity_usage', models.DecimalField(decimal_places=0, default=632, max_digits=6)),
                ('desired_system_capacity', models.DecimalField(decimal_places=1, default=0, max_digits=6)),
                ('your_current_electricity_provider', models.CharField(choices=[('PG&E', 'PG&E'), ('SF Clean Energy', 'SF Clean Energy'), ('Other', 'Other')], default='PGE', max_length=200)),
                ('roof_type', models.CharField(choices=[('Asphalt', 'Asphalt'), ('Corrugated', 'Corrugated'), ('Tile', 'Tile')], default='Asphalt', max_length=200)),
                ('stories', models.IntegerField(default=1)),
                ('cable_length', models.IntegerField(default=0)),
                ('busbar_capacity', models.IntegerField(default=100)),
                ('main_breaker_size', models.IntegerField(default=100)),
                ('is_there_room_for_new_breaker_opposite_main_breaker', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Help me figure it out', 'Help me figure it out')], default='Yes', max_length=200)),
                ('max_electrical_system_capacity_amps', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('max_electrical_system_capacity_kW', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('system_capacity', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('number_of_modules', models.IntegerField(default=0)),
                ('smartbox_size', models.IntegerField(default=0)),
                ('system_value', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('system_production', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('percent_of_electric_bill', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='House_Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_date', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy.House')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('credit_card_no', models.DecimalField(decimal_places=0, default=0, max_digits=16)),
                ('expiration_date', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('confirmation_code', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Receptacle_Installation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cost', models.CharField(max_length=200)),
                ('start_date_time', models.DateTimeField(null=True)),
                ('end_date_time', models.DateTimeField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy.Customer')),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buy.House')),
            ],
        ),
        migrations.CreateModel(
            name='Receptacle_Installer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('about', models.CharField(default='info about me here', max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, default=750, max_digits=9)),
                ('receptacle_installer_pic', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Receptacle_Installer_Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_date', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy.Receptacle_Installer')),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_size', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('cable_length', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('roof_peg_type', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('smartbox_size', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy.House')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('shipping_cost', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('tax', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy.Customer')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy.Payment_Method')),
                ('receptacle_installation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy.Receptacle_Installation')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy.System')),
            ],
        ),
        migrations.AddField(
            model_name='receptacle_installation',
            name='receptacle_installer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buy.Receptacle_Installer'),
        ),
    ]
