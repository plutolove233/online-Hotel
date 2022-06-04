#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

room_blueprint = Blueprint('room', __name__)

from . import urls
