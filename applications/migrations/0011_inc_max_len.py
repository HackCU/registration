# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-12-02 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0010_draft_app'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draftapplication',
            name='content',
            field=models.CharField(max_length=4000),
        ),
    ]
