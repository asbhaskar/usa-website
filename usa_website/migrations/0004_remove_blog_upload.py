# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-12-03 00:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa_website', '0003_auto_20171203_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='upload',
        ),
    ]