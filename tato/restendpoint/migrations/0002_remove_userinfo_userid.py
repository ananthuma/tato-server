# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-24 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restendpoint', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='userId',
        ),
    ]
