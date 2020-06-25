#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : urls.py
__time__    : 2020/6/26 0:27
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^sms/$', views.send_sms)
]