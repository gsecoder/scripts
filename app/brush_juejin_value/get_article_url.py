#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   get_article_url.py
@Time    :   2020/1/1611:01
@Author  :   crisimple
@Github :    https://juejin.im/user/5890963661ff4b006bebc3a5/posts
@Contact :   crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
import time

import random
import requests
from app.util.read_excel import ReadExcel


class GetArticle(object):
    ExcelPath = "../brush_juejin_value/brush_juejin_value.xlsx"
    SheetId = 0
    re = ReadExcel(excel_path=ExcelPath, sheet_id=SheetId)
    nrows = re.get_nrows()
    print("\033[91m%s\033[0m" % "[ReadExcel OK]\n")

    def __int__(self):
        pass

    def get_article_url(self):
        """"
        读取 excel 中测试用例的传入参数的字段值，请求接口
        :return: 返回接口请求的返回值
        """
        for i in range(1, self.nrows):
            IsExecute = self.re.get_cell(i, 0)
            ArticleName = self.re.get_cell(i, 1)
            ArticleUrl = self.re.get_cell(i, 2)
            ArticleViews = self.re.get_cell(i, 3)
            JP = self.re.get_cell(i, 4)

            if IsExecute:
                print(ArticleName)
                res = requests.get(url=ArticleUrl)
                time.sleep(random.randint(10, 30))


if __name__ == "__main__":
    ga = GetArticle()
    ga.get_article_url()