# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='url_to_ping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=200)),
                ('twitter_id', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]