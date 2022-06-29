#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:calc_time.py
# author:刘浩宇
# datetime: 2022/6/17 22:26
# software: PyCharm

"""
This is function description
"""

# import module your need
from datetime import datetime


class Calculate():
    @classmethod
    def calc_time_diff_days(cls, now: datetime, target: str):
        # 将 'cur_time' 类型时间通过格式化模式转换为 'str' 时间
        format_pattern = '%Y-%m-%d %H:%M:%S'
        cur_time = now.strftime(format_pattern)
        target_time = target
        difference = (datetime.strptime(target_time, format_pattern) - datetime.strptime(cur_time, format_pattern))
        return difference.days
