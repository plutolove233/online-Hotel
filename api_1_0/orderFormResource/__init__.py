#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

orderform_blueprint = Blueprint('orderForm', __name__)

from . import urls
