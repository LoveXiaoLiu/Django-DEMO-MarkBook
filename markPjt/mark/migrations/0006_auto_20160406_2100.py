# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mark', '0005_auto_20160406_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markbook',
            name='mark_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
