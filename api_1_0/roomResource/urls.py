#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import room_blueprint
from api_1_0.roomResource.roomResource import RoomResource
from api_1_0.roomResource.roomOtherResource import AddRoomResource

api = Api(room_blueprint)

api.add_resource(RoomResource, '/room/<RoomID>', '/room', endpoint='room')
api.add_resource(AddRoomResource, '/room/add', endpoint="add")