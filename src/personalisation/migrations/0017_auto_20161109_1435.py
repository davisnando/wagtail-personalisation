# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personalisation', '0016_auto_20161109_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='segment',
            name='edit_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
