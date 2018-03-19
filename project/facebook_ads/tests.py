# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Ad, Image, Link, Tag
# Create your tests here.

class AdTestCase(TestCase):
    tag_1 = None
    tag_2 = None
    image_1 = None
    image_2 = None
    image_3 = None
    link_1 = None
    link_2 = None
    link_3 = None
    ad_1 = None
    ad_2 = None

    def Setup(self):
        self.tag_1 = Tag.objects.create(attribute='functional')
        self.tag_2 = Tag.objects.create(attribute='emotional')
        self.image_1 = Image.objects.create(url='http://image1.com', attribute=self.tag_1)
        self.image_2 = Image.objects.create(url='http://image2.com', attribute=self.tag_1)
        self.image_3 = Image.objects.create(url='http://image3.com', attribute=self.tag_2)
        self.link_1 = Link.objects.create(url='http://link1.com', attribute=self.tag_1)
        self.link_2 = Link.objects.create(url='http://link2.com', attribute=self.tag_1)
        self.link_3 = Link.objects.create(url='http://link3.com', attribute=self.tag_2)
        self.ad_1 = Ad(name='myFirstAd',image=self.image_1, link=self.link_2)
        self.ad_2= Ad(name='mysecondAd',image=self.image_2, link=self.link_3)