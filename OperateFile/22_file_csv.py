#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   22_file_csv.py
@Time    :   2019/12/2210:42
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import os
import sys
import numpy as np
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print("BASE_DIR: %s" % BASE_DIR)
sys.path.append(BASE_DIR)


class OperateCsv(object):
    
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = "../OperateFile/data/csv.csv"
            
        self.df = self.read_csv()
        
    def read_csv(self):
        """
        filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，
        header=None表示头部为空，
        sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可
        @return: 返回CSV中的所有数据
        """
        df = pd.read_csv(
            self.file_name,
            header=None
        )
        return df
        
    def read_front_rows(self, n):
        """
        会包含表头的返回前n行的CSV数据
        @param n: 要返回的行数
        @return: 返回的 n 行数据
        """
        return self.df.head(n)
    
    def read_tail_rows(self, n):
        """
        返回CSV文件的最后 n 行数据
        @param n: 要返回的行数
        @return: 返回的后 n 行数据
        """
        return self.df.tail(n)
    
    def read_skiprows(self, *args):
        return pd.read_table(self.file_name, header=None, skiprows=args)
    
    def read_rows_cols(self, *args):
        drc = pd.read_csv(
            self.file_name,
            header=None,
            names=args
        )
        return drc


if __name__ == "__main__":
    oc = OperateCsv()
    # print("获取csv的所有数据：%s" % oc.read_csv())
    # print("获取前 %s 的数据: %s" % (4, oc.read_front_rows(4)))
    # print("获取后 %s 的数据: %s" % (3, oc.read_tail_rows(3)))
    print("获取数据跳过某些行: %s" % (oc.read_skiprows(0, 1, 2)))
    # print("获取指定列" % oc.read_rows_cols('start_time', 'id'))

