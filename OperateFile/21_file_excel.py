#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   21_file_excel.py
@Time    :   2019/12/21下午2:46
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import os
import sys
import xlrd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
print("BASE_DIR: %s" % BASE_DIR)


class OperateExcel(object):

    def __init__(self, file_name=None, sheet_id=None):
        """
        获取要读取的excel文件
        :param file_name: 文件名称
        :param sheet_id: 文件的sheet页
        """
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = "../OperateFile/data/excel.xlsx"

        if sheet_id:
            self.sheet_id = sheet_id
        else:
            self.sheet_id = 0

        self.sheet_table = self.get_sheet()

    # 获取 sheet 页的操作对象
    def get_sheet(self):
        data = xlrd.open_workbook(self.file_name)
        sheet_table = data.sheets()[self.sheet_id]
        return sheet_table

    # 获取 sheet 页的行数和列数，返回的是一个元祖
    def get_sheet_nrows_ncols(self):
        return self.sheet_table.nrows, self.sheet_table.ncols

    # 获取 sheet 页的行数（Excel中常用到）
    def get_sheet_nrows(self):
        return self.sheet_table.nrows

    # 获取 sheet 页的列数
    def get_sheet_ncols(self):
        return self.sheet_table.ncols

    # 获取单元格中的数据
    def get_sheet_cell(self, row, col):
        """
        :param row: 单元格的第几行
        :param col: 单元格的第几列
        :return: 单元格的值
        """
        cell_data = self.sheet_table.cell_value(row, col)
        return cell_data


if __name__ == "__main__":
    oe = OperateExcel()
    print("获取Excel对象：%s" % oe.get_sheet())
    print("Excel有：(%s, %s)" % oe.get_sheet_nrows_ncols())
    print("Excel有：%s 行" % oe.get_sheet_nrows())
    print("Excel有：%s 列" % oe.get_sheet_ncols())
    print("Excel的第 %s 行 %s 列的值为： %s" % (2, 2, oe.get_sheet_cell(2, 2)))
