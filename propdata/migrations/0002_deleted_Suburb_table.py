# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-10 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propdata', '0001_prop_add_all_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housedetails',
            name='suburb',
            field=models.CharField(choices=[('CW', 'Cowies Hill'), ('CH', 'Chiltern Hills'), ('DC', 'Dawncliffe'), ('RC', 'Reservoir Hills'), ('AH', 'Atholl Heights'), ('BW', 'Berea West'), ('RK', 'Rooikoppies'), ('WV', 'Westville'), ('CM', 'Cato Manor'), ('AS', 'Asherville'), ('SW', 'Sherwood'), ('CE', 'Clare Estate')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Suburb',
        ),
    ]
