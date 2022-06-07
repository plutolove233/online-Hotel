#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import hotel_blueprint
from api_1_0.hotelResource.hotelResource import HotelResource
from api_1_0.hotelResource.hotelOtherResource import HotelRegisterResource

api = Api(hotel_blueprint)

api.add_resource(HotelResource, '/hotel/<HotelID>', '/hotel', endpoint='hotel')
api.add_resource(HotelRegisterResource, '/hotel/register', endpoint="register")
