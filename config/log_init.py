#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : log_init.py
__time__    : 2020/6/20 21:13
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

import logging

# 创建 logger 对象
logger = logging.getLogger()

# 设置 log 级别
logger.setLevel(logging.DEBUG)

# 日志存放目录
log_file = "../log/log.log"

# 追加日志
fh = logging.FileHandler(log_file, mode="a")
fh.setLevel(logging.DEBUG)

# 创建一个 handler，用于输出控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# handler的输出格式
formatter = logging.Formatter(
    "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)"
)
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

# 日志
logger.debug(u'这是 logger debug message')
logger.info(u'这是 logger info message')
logger.warning(u'这是 logger warning message')
logger.error(u'这是 logger error message')
logger.critical(u'这是 logger critical message')
