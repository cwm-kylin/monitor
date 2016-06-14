# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
     url(r'^$','webmonitor.views.index'),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^admin/', include(admin.site.urls)),
     url(r'add_do/','webmonitor.views.adddo'),
    url(r'add/','webmonitor.views.add'),
    url(r'monitorlist/','webmonitor.views.monitorlist'),


)
