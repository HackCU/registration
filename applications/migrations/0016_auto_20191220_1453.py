# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-12-20 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0015_auto_20191219_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='graduation_year',
            field=models.IntegerField(choices=[(2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024')], default=2019),
        ),
    ]
