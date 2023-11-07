#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : urls.py
__time__    : 2020/5/31 16:02
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)/(\d+)$', views.detail),

    # 在blog下分化url
    url(r'^grades/$', views.grades),
    url(r'^student/$', views.student),
    url(r'^grades/(\d+)$', views.gradeStudent)
]
