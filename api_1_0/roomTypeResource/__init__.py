#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

roomtype_blueprint = Blueprint('roomType', __name__)

from . import urls
