# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markbook',
            name='mark_belong',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mark.markbookDIR'),
        ),
    ]
