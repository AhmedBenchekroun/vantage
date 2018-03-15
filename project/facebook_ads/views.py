# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is it!</h1>")

def find_ad_by_id(request, ad_id):
    return HttpResponse("<h1>Ad id:" + str(ad_id) + "</h1>")
# Create your views here.
