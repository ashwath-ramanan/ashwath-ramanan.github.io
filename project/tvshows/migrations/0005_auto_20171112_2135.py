# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0004_auto_20171110_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvseries',
            name='link',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tvseries',
            name='vlink',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
