# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0005_auto_20161105_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relative',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
