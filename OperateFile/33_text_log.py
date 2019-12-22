#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   33_text_log.xml
@Time    :   2019/12/2216:18
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import os
import sys
import logging
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
LOG_FORMAT = "%(asctime)s=====%(levelname)s+++++%(message)s"

class OperateLog():
    def __int__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = "../OperateFile/logs/"
            
    def write_log1(self, file_name=None, message=None):
        logging.basicConfig(
            filename=file_name,
            level=logging.DEBUG,
            format=LOG_FORMAT
        )
        logging.debug(message)
        logging.info(message)
        logging.warning(message)
        logging.error(message)
        logging.critical(message)
        
    def write_log2(self, file_name=None, message=None):
        """
        :param file_name: 日志路径
        :param message: 要写入的日志信息
        :return:
        """
        logging.basicConfig(
            filename=file_name,
            level=logging.DEBUG,
            format=LOG_FORMAT
        )
        logging.log(logging.DEBUG, message)
        logging.log(logging.INFO, message)
        logging.log(logging.WARNING, message)
        logging.log(logging.ERROR, message)
        logging.log(logging.CRITICAL, message)
        
        
if __name__ == "__main__":
    ol = OperateLog()
    log_times = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    file_name_1 = "./logs/%s_log.log" % log_times
    # ol.write_log1(file_name_1)
    
    file_name_2 = "./logs/%s_log.log" % log_times
    # ol.write_log2(file_name_2)
