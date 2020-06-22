#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : s_logging.py
__time__   : 2020/6/22 10:45
__author__ : crisimple
__resume__ : None

__日志等级从高到底排序__：
    FATAL       --- 致命错误、
    CRITICAL    --- 特别糟糕的事情，如内存耗尽、磁盘空间为空，一般很少使用
    ERROR       --- 发生错误时，如IO操作失败或者连接问题
    WARNING     --- 发生很重要的事件，但是并不是错误时，如用户登录密码错误
    INFO        --- 处理请求或者状态变化等日常事务
    DEBUG       --- 调试过程中使用DEBUG等级，如算法中每个循环的中间状态
"""
import logging

from logging.handlers import RotatingFileHandler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 定义一个 RotatingFileHandler，最多备份 3 个日志文件，每个日志文件最大 1k
rHandler = RotatingFileHandler("../data/s_logging_exception.log", maxBytes=1*1024, backupCount=3)
rHandler.setLevel(level=logging.INFO)
rHandler.setFormatter(formatter)

logger = logging.getLogger(__name__)

# 将日志写入到文件中
# handler = logging.FileHandler("../data/s_logging_log.log")
# handler.setLevel(level=logging.INFO)

rHandler.setFormatter(formatter)
logger.addHandler(rHandler)

# 将日志同时输出到屏幕和日志文件
console = logging.StreamHandler()
console.setLevel(level=logging.INFO)
logger.addHandler(console)


logger.info("info start")
logger.debug("debug")
logger.warning("warning")
logger.fatal("fatal")
logger.critical("critical")
logger.error("error")
try:
    open("../data/mysql.inis", "rb")
except (SystemExit, KeyboardInterrupt):
    raise
except Exception:
    logger.exception("Failed to open mysql.inis from logger.exception")
    # 等价于下面的代码，用一个就好
    # logger.error("Failed to open mysql.inis from logger.error", exc_info=True)
logger.info("info end")
