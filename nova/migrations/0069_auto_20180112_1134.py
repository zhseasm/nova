# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-01-12 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0068_auto_20180110_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='areceiver',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='\u63a5\u6536\u8005'),
        ),
        migrations.AddField(
            model_name='mail',
            name='password',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='\u5bc6\u7801'),
        ),
        migrations.AddField(
            model_name='mail',
            name='smtp_port',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='smtp\u7aef\u53e3'),
        ),
        migrations.AddField(
            model_name='mail',
            name='smtp_server',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='smtp\u670d\u52a1\u5668'),
        ),
        migrations.AddField(
            model_name='mail',
            name='user',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='\u7528\u6237\u540d'),
        ),
    ]
