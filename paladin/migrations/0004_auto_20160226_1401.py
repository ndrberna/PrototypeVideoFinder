# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paladin', '0003_delete_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='text',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='result',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
