#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:urls.py
# author:刘浩宇
# datetime: 2022/6/5 19:52
# software: PyCharm

"""
This is function description
"""
from flask_restful import Api

from . import login_blueprint
from api_1_0.apiCommonResource.loginResource import LoginResource
from api_1_0.apiCommonResource.sendEmailResource import SendEmailResource
from api_1_0.apiCommonResource.changePasswordResource import ChangePwdResource


api = Api(login_blueprint)
api.add_resource(LoginResource, '/login', endpoint='login')
api.add_resource(SendEmailResource, '/send_email', endpoint="send_email")
api.add_resource(ChangePwdResource, '/change_pwd', endpoint="change_pwd")