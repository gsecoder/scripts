#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : tests_models.py
__author__ : jiangheng
__date__   : 2020-05-26 15:32
__function__: models.py unit test
"""

import os
import sys
from django.test import TestCase
from .models import Article

current_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(current_path)[0]
sys.path.append(root_path)


class TestArticle(TestCase):
    def setUp(self):
        self.title1 = '测试文章1'
        self.content1="测试文章1测试文章1"
        self.title2 = '测试文章2'
        self.content2="测试文章1测试文章2"
        Article.objects.create(title=self.title1, content=self.content1)
        Article.objects.create(title=self.title2, content=self.content2)

    def test_add_article_success(self):
        articles_title = []
        articles = Article.objects.all()
        for article in articles:
            articles_title.append(article.title)
        # print(articles_title)
        if self.title1 in articles_title and self.title2 in articles_title:
            print("创建数据成功")
        else:
            print("创建数据失败")

    def tearDown(self):
        Article.objects.filter(title__in=['测试文章']).delete()



