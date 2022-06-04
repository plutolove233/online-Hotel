#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

hotel_blueprint = Blueprint('hotel', __name__)

from . import urls
