# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Facebook_Ad(models.model):
    name = models.CharField(max_length=255)
    image_url = models.ForeignKey(Image, on_delete=models.CASCADE)
    link_url = models.ForeignKey(Link, on_delete=models.CASCADE)

class Image(models.model):
    url = models.CharField(max_length=255)
    image_attribute = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Link(models.model):
    url = models.CharField(max_length=255)
    link_attribute = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Tag(models.model):
    attribute = models.CharField(max_length=255)