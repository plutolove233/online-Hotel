#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import user_blueprint
from api_1_0.userResource.userResource import UserResource
from api_1_0.userResource.userOtherResource import UserRegisterResource

api = Api(user_blueprint)

api.add_resource(UserResource, '/user/<UserID>', '/user', endpoint='user')
api.add_resource(UserRegisterResource, "/user/register", endpoint='register')