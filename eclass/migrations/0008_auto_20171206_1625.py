# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 16:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eclass', '0007_auto_20171206_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incompleted_assignment',
            name='assignment',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.CharField(choices=[('Finished', 'Finished'), ('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive', max_length=20),
        ),
        migrations.AlterField(
            model_name='completed_assignment',
            name='time',
            field=models.DateField(default=datetime.datetime(2017, 12, 6, 16, 25, 29, 534638)),
        ),
        migrations.AlterField(
            model_name='note',
            name='file_type',
            field=models.CharField(blank=True, choices=[('Image', 'Image'), ('Other', 'Other')], default='Image', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
        migrations.DeleteModel(
            name='incompleted_assignment',
        ),
    ]
