#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

remark_blueprint = Blueprint('remark', __name__)

from . import urls
