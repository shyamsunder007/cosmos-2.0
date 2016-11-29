# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-25 13:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('btp', '0012_auto_20161118_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmedia',
            name='file_name',
            field=models.TextField(default=b'no name provided'),
        ),
        migrations.AlterField(
            model_name='btpsetweek',
            name='evalday',
            field=models.DateField(default=datetime.datetime(2016, 11, 25, 13, 14, 4, 180107, tzinfo=utc)),
        ),
    ]