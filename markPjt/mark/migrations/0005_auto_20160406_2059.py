# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mark', '0004_auto_20160406_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markbook',
            name='mark_url',
            field=models.CharField(max_length=500),
        ),
    ]
