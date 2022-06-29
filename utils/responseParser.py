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
from utils.response_code import RET, error_map_CN


class ResponseParser():
    @classmethod
    def parse_param_error(cls, **kwargs):
        return {
            'code': RET.PARAMERR,
            "message": "获取请求参数失败",
            'error': kwargs.get('error')
        }

    @classmethod
    def parse_ok(cls, message, **kwargs):
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
    def parse_list_ok(cls, message, li: list):
        return {
            "code": RET.OK,
            "message": message,
            "data": li,
        }

    @classmethod
    def parse_res(cls, **kwargs):
        return {
            "code": kwargs.get("code"),
            "message": kwargs.get("message"),
            "error": kwargs.get('data').get("error"),
        }

    @classmethod
    def parse_no_data(cls, **kwargs):
        return {
            "code": RET.NODATA,
            "message": kwargs.get("message")
        }

    @classmethod
    def parse_unknown_error(cls, **kwargs):
        return {
            "code": RET.UNKOWNERR,
            "error": kwargs.get("error"),
            "message": "未知错误",
        }

    @classmethod
    def parse_role_error(cls):
        return {
            "code": RET.ROLEERR,
            "message": "用户类型不匹配",
        }

    @classmethod
    def parse_db_error(cls, **kwargs):
        return {
            "code": RET.DBERR,
            "error": kwargs.get("error"),
            "message": error_map_CN[RET.DBERR],
        }
