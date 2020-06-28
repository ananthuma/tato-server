# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils.datetime_safe import datetime


class UserInfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    about = models.CharField(max_length=1024)
    userId = models.CharField(max_length=255)
    active = models.BooleanField(blank=True, default=False)
    password = models.CharField(max_length=255, blank=True, default=datetime.now)
    salt = models.CharField(max_length=255, blank=True, default=datetime.now)
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True, default=datetime.now)
    phone = models.CharField(max_length=255, blank=True,default=datetime.now)
    imgurl = models.URLField(default='')

class Status(models.Model):
    statusId = models.CharField(max_length=255)
    userId = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    visibility = models.CharField(max_length=255)
    url = models.URLField()
    text = models.CharField(max_length=255)
    time = models.TimeField(auto_now=True)
    category = models.CharField(max_length=255)



