# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-10 20:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propdata', '0004_added_validation_to_email_and_integerFields'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='agent',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]