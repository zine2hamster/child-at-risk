# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0002_auto_20161104_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'female')], max_length=2)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
