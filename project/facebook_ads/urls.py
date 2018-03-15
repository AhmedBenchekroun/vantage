from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<ad_id>[0-9]+)$', views.find_ad_by_id, name='find_ad_by_id')
]