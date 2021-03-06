# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 15:42
from __future__ import unicode_literals

import bravitzlana.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bravitzlana', '0002_game_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_new_template',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='session_key',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='game',
            name='save_data',
            field=models.FileField(upload_to=bravitzlana.models.generate_save_path),
        ),
    ]
