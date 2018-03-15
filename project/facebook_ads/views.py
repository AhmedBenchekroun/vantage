# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Ad

def index(request):
    all_ads = Ad.objects.all()
    html = ""
    for ad in all_ads:
        url = '/facebook_ads/' + str(ad.id) + "/"
        html += '<a href="' + url + '">' + ad.name + "</a></ br>"
    return HttpResponse(html)

def find_ad_by_id(request, ad_id):
    return HttpResponse("<h1>Ad id:" + str(ad_id) + "</h1>")
# Create your views here.
