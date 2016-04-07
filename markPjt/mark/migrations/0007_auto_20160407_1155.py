# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 03:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mark', '0006_auto_20160406_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markbook',
            name='create_time',
            field=models.CharField(blank=True, max_length=20, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='markbook',
            name='mark_belong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mark.markbookDIR', verbose_name='\u6240\u5c5e\u4e66\u7b7e\u5939'),
        ),
        migrations.AlterField(
            model_name='markbook',
            name='mark_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='\u4e66\u7b7e\u540d'),
        ),
        migrations.AlterField(
            model_name='markbook',
            name='mark_url',
            field=models.CharField(max_length=500, verbose_name='URL\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='markbookdir',
            name='dir_info',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='markbookdir',
            name='dir_name',
            field=models.CharField(max_length=200, unique=True, verbose_name='\u4e66\u7b7e\u5939'),
        ),
    ]
