# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-04 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gp', '0003_auto_20160220_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=20)),
                ('Note', models.TextField()),
            ],
        ),
    ]
