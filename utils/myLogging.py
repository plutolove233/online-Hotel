#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:myLogging.py
# author:刘浩宇
# datetime: 2022/6/6 15:23
# software: PyCharm

"""
This is function description
"""

# import module your need
import os
import logging
import re
from logging.handlers import TimedRotatingFileHandler


def setup_log(log_name):
    # 创建logger对象。传入logger名字
    try:
        print("loading log...")
        logger = logging.getLogger(log_name)
        log_path = os.path.join(r"./logs", log_name)
        # 设置日志记录等级
        logger.setLevel(logging.INFO)
        # interval 滚动周期，
        # when="MIDNIGHT", interval=1 表示每天0点为更新点，每天生成一个文件
        # backupCount  表示日志保存个数
        file_handler = TimedRotatingFileHandler(
            filename=log_path, when="MIDNIGHT", interval=1, backupCount=7
        )
        # filename="mylog" suffix设置，会生成文件名为mylog.2020-02-25.log
        file_handler.suffix = "%Y-%m-%d.log"
        # extMatch是编译好正则表达式，用于匹配日志文件名后缀
        # 需要注意的是suffix和extMatch一定要匹配的上，如果不匹配，过期日志不会被删除。
        file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
        # 定义日志输出格式
        file_handler.setFormatter(
            logging.Formatter(
                "[%(asctime)s] [%(process)d] [%(levelname)s] - %(module)s.%(funcName)s (%(filename)s:%(lineno)d) - %(message)s"
            )
        )
        logger.addHandler(file_handler)
        return logger
    except Exception as e:
        print(e)
        print(str(e))


logger = setup_log("system.log")
