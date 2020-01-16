#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   read_excel.py
@Time    :   2020/1/1519:09
@Author  :   crisimple
@Github :    https://juejin.im/user/5890963661ff4b006bebc3a5/posts
@Contact :   crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
import xlrd

class ReadExcel(object):

    def __init__(self, excel_path=None, sheet_id=None):
        """
        根据输入 excel 表路径来读取 excel，没有传的话，默认为读取 "../brush_juejin_value/brush_juejin_value.xlsx"
        根据输入 sheet 页来操作数据，没有传 sheet 页的话，默认为第 1 sheet 页
        :param excel_path: 读取的 excel 路径
        :param sheet_id: 要操作的 sheet 页
        :return: 操作数据对象
        """
        if excel_path:
            self.excel_path = excel_path
        else:
            self.excel_path = '../brush_juejin_value/brush_juejin_value.xlsx'

        if sheet_id:
            self.sheet_id = sheet_id
        else:
            self.sheet_id = 0

        self.get_data = self.get_sheet()

    def get_sheet(self):
        """
        打开要操作的 excel 文件，并读取 excel 指定 sheet 页的数据
        :return: excel 指定 sheet 页的数据对象
        """
        data = xlrd.open_workbook(self.excel_path)
        sheet_data = data.sheets()[self.sheet_id]
        return sheet_data

    def get_nrows_ncols(self):
        """
        获取 sheet 页的行数和列表，返回的是一个元组
        :return: (行数, 列数)
        """
        return self.get_data.nrows, self.get_data.ncols

    def get_nrows(self):
        """
        获取行数
        :return: 返回行数
        """
        return self.get_data.nrows

    def get_ncols(self):
        """
        获取列数
        :return: 返回列数
        """
        return self.get_data.ncols

    # 获取单元格的值
    def get_cell(self, row, col):
        """
        row: 第几行
        col: 第几列
        cell_data: 单元格值
        """
        cell_data = self.get_data.cell_value(row, col)
        return cell_data


if __name__ == "__main__":
    er = ReadExcel()
    print(er.get_nrows())
