# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-24 15:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restendpoint', '0002_remove_userinfo_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='userId',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
