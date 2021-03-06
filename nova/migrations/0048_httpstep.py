# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-14 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0047_auto_20171205_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='HttpStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u670d\u52a1\u540d\u79f0')),
                ('url', models.CharField(max_length=2000, verbose_name='\u670d\u52a1URL')),
                ('timeout', models.CharField(default=b'15s', max_length=20, verbose_name='\u8d85\u65f6\u65f6\u95f4')),
                ('required', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u8fd4\u56de\u6bd4\u8f83\u503c')),
                ('status_codes', models.CharField(max_length=100, verbose_name='\u8fd4\u56de\u72b6\u6001\u7801')),
                ('step_field', models.CharField(blank=True, max_length=2000, null=True, verbose_name='\u8bf7\u6c42\u53c2\u6570')),
                ('post_type', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8bf7\u6c42\u7c7b\u578b')),
            ],
        ),
    ]
