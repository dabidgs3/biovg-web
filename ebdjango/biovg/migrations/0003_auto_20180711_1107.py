# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-07-11 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biovg', '0002_auto_20180624_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=4000)),
            ],
        ),
        migrations.AlterField(
            model_name='service_section',
            name='description',
            field=models.CharField(max_length=4000),
        ),
    ]