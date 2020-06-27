#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : urls.py
__time__    : 2020/6/26 0:27
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

import os, sys
from django.conf.urls import url
from web.views import account

urlpatterns = [
    url(r'^$', account.index, name="index"),
    url(r'^sms/$', account.send_sms, name="send_sms"),
    url(r'^register/$', account.register, name="register")
]

