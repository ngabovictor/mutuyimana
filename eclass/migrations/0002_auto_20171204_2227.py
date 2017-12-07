# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 22:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eclass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.CharField(choices=[('Inactive', 'Inactive'), ('Finished', 'Finished'), ('Active', 'Active')], default='Inactive', max_length=20),
        ),
        migrations.AlterField(
            model_name='completed_assignment',
            name='time',
            field=models.DateField(default=datetime.datetime(2017, 12, 4, 22, 27, 10, 132255)),
        ),
        migrations.AlterField(
            model_name='note',
            name='file_type',
            field=models.CharField(blank=True, choices=[('Other', 'Other'), ('Image', 'Image')], default='Image', max_length=200, null=True),
        ),
    ]