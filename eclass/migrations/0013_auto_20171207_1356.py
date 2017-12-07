# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 13:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eclass', '0012_auto_20171207_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Finished', 'Finished')], default='Inactive', max_length=20),
        ),
        migrations.AlterField(
            model_name='completed_assignment',
            name='time',
            field=models.DateField(default=datetime.datetime(2017, 12, 7, 13, 56, 5, 15088)),
        ),
    ]