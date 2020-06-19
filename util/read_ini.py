#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : read_ini.py 
__author__ : jiangheng
__date__   : 2020-06-04 17:44
__function__:
    读取 ini 文件
"""
import configparser

class ReadIni(object):

    def __init__(self, ini_file=None, node=None):
        if ini_file:
            self.ini_file = ini_file
        else:
            self.ini_file = "../data/mysql.ini"

        if node:
            self.node = node
        else:
            self.node = 'login_info'

        self.cf = configparser.ConfigParser()
        self.cfr = self.cf.read(self.ini_file)

    def read_ini(self, node, key):
        val = self.cf.get(node, key)
        return val


if __name__ == "__main__":
    ri = ReadIni()
    print(ri.read_ini('login_info', 'i_host'))