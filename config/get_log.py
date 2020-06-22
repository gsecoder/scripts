#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : get_log.py
__time__    : 2020/6/20 21:13
__author__  : crisimple
__github__ :  https://github.com/crisimple
"""

import logging
from logging.handlers import RotatingFileHandler

def get_logger(args_log_file, args_log_level, args_log_msg):
    # 创建 logger 对象
    logger = logging.getLogger()

    # 设置 log 级别
    # logger.setLevel(logging.DEBUG)

    # 设置 log 输出的格式
    formatter = logging.Formatter(
        "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
    )

    # 定义一个 RotatingFileHandler 对象，最多备份 10 个日志文件，每个日志文件，每个日志文件10k
    rHandler = RotatingFileHandler(
        filename=args_log_file,
        maxBytes=10*1024,
        backupCount=10,
        mode="a"
    )
    # 设置记录日志的等级
    rHandler.setLevel(level=args_log_level)
    rHandler.setFormatter(formatter)
    logger.addHandler(rHandler)
    logger.fatal(args_log_msg)
    logger.critical(args_log_msg)
    logger.error(args_log_msg)
    logger.warning(args_log_msg)
    logger.info(args_log_msg)
    logger.debug(args_log_msg)


if __name__ == '__main__':
    get_logger(
        args_log_file="../log/get_log.log",
        args_log_level=logging.DEBUG,
        args_log_msg="test"
    )
