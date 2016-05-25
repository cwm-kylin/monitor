# -*- coding: utf-8 -*-

from django import template
from publicclass.views import *
from django.conf import settings

register = template.Library()

def result_domain(value):
    return GetURLdomain(value)
    
def result_datetime(value):
    return stamp2time(value)

def result_idcname(value):
    return settings.IDC[value]


register.filter(result_domain)
register.filter(result_datetime)
register.filter(result_idcname)
