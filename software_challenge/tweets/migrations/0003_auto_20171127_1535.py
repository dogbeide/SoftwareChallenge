# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-27 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='handle',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(max_length=140, unique=True),
        ),
    ]
