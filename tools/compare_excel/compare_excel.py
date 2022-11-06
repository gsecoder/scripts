#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
__file__   : compare_excel
__time__   : 2022/9/2 00:25
__author__ : secoder
__resume__ : None
"""

import xlrd
import os


class CompareExcel(object):

    def __int__(self, file1, file2):
        print("初始化读取")
        # 获取要对比的源文件和目标文件
        self.origin = os.path.join(os.getcwd(), file1)
        self.target = os.path.join(os.getcwd(), file2)

        # 获取操作句柄
        self.workbook1 = xlrd.open_workbook(self.origin)
        self.workbook2 = xlrd.open_workbook(self.target)

    def compare_excel(self):
        # 获取Excel要对比sheet的对象
        origin = self.workbook1.sheets()[0]
        target = self.workbook2.sheets()[0]

        # 获取origin的行数
        origin_nrows = origin.nrows
        for i in range(origin_nrows):
            print("i: ", i)


if __name__ == '__main__':
    origin_excel = './origin.xlsx'
    target_excel = './target.xlsx'
    ce = CompareExcel()
    ce.compare_excel()