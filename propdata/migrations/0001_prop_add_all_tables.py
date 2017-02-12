# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-10 03:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('cellPhone', models.IntegerField()),
                ('picture', models.ImageField(upload_to='pictures')),
            ],
        ),
        migrations.CreateModel(
            name='HouseDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrooms', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('picture', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('marketingHeading', models.CharField(max_length=50)),
                ('ownersRefNumber', models.CharField(max_length=50)),
                ('associated_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propdata.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propdata.HouseDetails')),
            ],
        ),
        migrations.CreateModel(
            name='Suburb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suburb_name', models.CharField(choices=[('CW', 'Cowies Hill'), ('CH', 'Chiltern Hills'), ('DC', 'Dawncliffe'), ('RC', 'Reservoir Hills'), ('AH', 'Atholl Heights'), ('BW', 'Berea West'), ('RK', 'Rooikoppies'), ('WV', 'Westville'), ('CM', 'Cato Manor'), ('AS', 'Asherville'), ('SW', 'Sherwood'), ('CE', 'Clare Estate')], max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='housedetails',
            name='suburb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propdata.Suburb'),
        ),
    ]