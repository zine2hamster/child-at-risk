# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0009_home_parent_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='parent_home',
            field=models.CharField(default='', max_length=20),
        ),
    ]
