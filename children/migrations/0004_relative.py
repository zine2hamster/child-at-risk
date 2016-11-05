# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0003_home_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'female')], max_length=2)),
                ('phone', models.CharField(max_length=20)),
                ('relationship', models.CharField(max_length=20)),
                ('relatedTo', models.ManyToManyField(to='children.Child')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
