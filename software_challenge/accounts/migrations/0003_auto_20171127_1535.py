# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-27 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_logininstance_logoutinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='logininstance',
            name='username',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='logoutinstance',
            name='username',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
    ]