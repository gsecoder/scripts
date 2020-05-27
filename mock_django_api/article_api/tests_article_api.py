#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : tests_article_api.py
__author__ : jiangheng
__date__   : 2020-05-27 9:32
__function__: 测试 article_api 创建的接口
"""
# from django.test import TestCase
# from django.test import RequestFactory      # RequestFactory：django自身集成的测试套件
# from .views import Article
#
# import sys
# import os
# current_path = os.path.abspath(os.path.dirname(__file__))
# root_path = current_path.split(current_path)[0]
# sys.path.append(root_path)
#
#
# class TestArticleApi(TestCase):
#
#     def setUp(self):
#         self.title1 = '测试文章1'
#         self.content1="测试文章1测试文章1"
#         self.factory = RequestFactory()
#         self.article = Article.objects.create(title=self.title1, content=self.content1)
#         self.article.save()
#
#     def test_query_article(self):
#         request = self.factory.get('/query_article')
#         print("request: ", request)
#
#
# if __name__ == "__main__":
#     TestArticleApi.test_query_article()