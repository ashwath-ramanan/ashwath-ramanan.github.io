# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0006_animeseries_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='animeseries',
            name='link1',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
