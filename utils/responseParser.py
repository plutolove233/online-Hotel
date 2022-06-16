#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:responseParser.py
# author:刘浩宇
# datetime: 2022/6/16 16:34
# software: PyCharm

"""
This is function description
"""

# import module your need
from utils.response_code import RET


class ResponseParser():
    @classmethod
    def parse_ok(cls,message, **kwargs):
        if kwargs is not None:
            return {
                "code": RET.OK,
                "message": message,
                "data": kwargs,
            }
        return {
            "code": RET.OK,
            "message": message,
        }

    @classmethod
    def parse_res(cls, **kwargs):
        return {
            "code": kwargs.get("code"),
            "message": kwargs.get("message"),
            "error": kwargs.get("error"),
        }

    @classmethod
    def parse_no_data(cls, **kwargs):
        return {
            "code": RET.NODATA,
            "message": kwargs.get("message")
        }
