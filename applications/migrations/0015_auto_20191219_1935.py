# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-12-20 02:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0014_fix_tshirt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='lennyface',
        ),
        migrations.RemoveField(
            model_name='application',
            name='phone_number',
        ),
    ]
