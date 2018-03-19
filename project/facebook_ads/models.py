# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Tag(models.Model):
    attribute = models.CharField(max_length=255)

class Image(models.Model):
    url = models.CharField(max_length=255)
    image_attribute = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)

class Link(models.Model):
    url = models.CharField(max_length=255)
    link_attribute = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)

class Tag_Image(models.Model):
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Tag_Link(models.Model):
    link_id = models.ForeignKey(Link, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Ad(models.Model):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
