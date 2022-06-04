#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import room_blueprint
from api_1_0.roomResource.roomResource import RoomResource
from api_1_0.roomResource.roomOtherResource import RoomOtherResource

api = Api(room_blueprint)

api.add_resource(RoomResource, '/room/<RoomID>', '/room', endpoint='room')
