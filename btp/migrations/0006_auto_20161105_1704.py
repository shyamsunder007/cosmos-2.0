# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-05 11:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('btp', '0005_auto_20160906_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='btpproject',
            name='year',
            field=models.CharField(default=b'2015', max_length=4),
        ),
        migrations.AlterField(
            model_name='btpsetweek',
            name='evalday',
            field=models.DateField(default=datetime.datetime(2016, 11, 5, 11, 34, 30, 400003, tzinfo=utc)),
        ),
    ]
