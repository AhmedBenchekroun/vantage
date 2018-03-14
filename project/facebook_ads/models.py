# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Facebook_Ad(models.model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255)
