# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-16 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bravitzlana', '0003_auto_20170426_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_tutorial_game',
            field=models.BooleanField(default=False),
        ),
    ]
