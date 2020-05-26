#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : test_models.py 
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
        pass
        Article.objects.create(title='测试文章1', content="测试文章1测试文章1")
        # Article.objects.create(title='测试文章2', content="测试文章2测试文章2")

    def test_add_article_success(self):
        articles_title = []
        articles = Article.objects.all()
        for article in articles:
            articles_title.append(article.title)
        # print(articles_title)
        self.assertIn("测试文章1", articles_title)

    def tearDown(self):
        Article.objects.filter(title__in=['测试文章']).delete()



