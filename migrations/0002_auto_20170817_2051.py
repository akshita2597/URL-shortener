# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-17 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
