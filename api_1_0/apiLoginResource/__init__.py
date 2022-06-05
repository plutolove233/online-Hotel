#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:__init__.py.py
# author:刘浩宇
# datetime: 2022/6/5 19:50
# software: PyCharm

"""
This is function description
"""

from flask import Blueprint

login_blueprint = Blueprint('login',__name__)

from . import urls