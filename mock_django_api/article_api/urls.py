#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : urls.py 
__author__ : jiangheng
__date__   : 2020-05-27 11:37
__function__:
"""
from django.urls import path
from . import views

# app_name 设置命名空间
app_name = "article_api"

urlpatterns = [
    path('', views.index, name="index"),
    path('index_detail/<int:article_id>/', views.index_detail, name="index_detail"),
    path('query/', views.query, name='query_article'),
    path('add/', views.add, name='add_article'),
    path('update/<int:article_id>', views.update, name='update_article'),
    path('delete/<int:article_id>', views.delete, name='delete_article'),
]