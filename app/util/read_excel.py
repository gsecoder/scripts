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

    def __int__(self, excel_path, sheet_id):

        if excel_path:
            self.excel_path = excel_path
        else:
            self.excel_path = "../brush_juejin_value/brush_juejin_value.xlsx"

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
        print(type(sheet_data))
        # return sheet_data


if __name__ == "__main__":
    re = ReadExcel()
    re.get_sheet()