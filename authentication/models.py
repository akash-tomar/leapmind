# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RecoveryToken(models.Model):
	email = models.EmailField(unique=True)
	token = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now=True)