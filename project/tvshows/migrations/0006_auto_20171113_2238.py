# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0005_auto_20171112_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tvseries',
            old_name='link',
            new_name='plink',
        ),
        migrations.RemoveField(
            model_name='tvseries',
            name='vlink',
        ),
        migrations.AddField(
            model_name='seasons',
            name='plink',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]
