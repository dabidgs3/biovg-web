# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-06-23 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
    ]
