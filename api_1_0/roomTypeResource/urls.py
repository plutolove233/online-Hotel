#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import roomtype_blueprint
from api_1_0.roomTypeResource.roomTypeResource import RoomTypeResource
from api_1_0.roomTypeResource.roomTypeOtherResource import AddRoomTypeResource

api = Api(roomtype_blueprint)

api.add_resource(RoomTypeResource, '/roomType/<RoomTypeID>', '/roomType', endpoint='roomType')
api.add_resource(AddRoomTypeResource, '/roomType/add', endpoint="add")