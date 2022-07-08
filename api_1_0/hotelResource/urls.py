#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import hotel_blueprint
from api_1_0.hotelResource.hotelResource import HotelResource
from api_1_0.hotelResource.hotelOtherResource import HotelRegisterResource, QueryHotelRoomsInfoResource
from api_1_0.hotelResource.hotelOtherResource import ChangeHotelInfoResource, OrderFormCheckOutResource, \
    OrderFormCheckInResource, QueryHotelOrderFormListResource

api = Api(hotel_blueprint)

api.add_resource(HotelResource, '/hotel/<HotelID>', '/hotel', endpoint='hotel')
api.add_resource(HotelRegisterResource, '/hotel/register', endpoint="register")
api.add_resource(ChangeHotelInfoResource, '/hotel/change', endpoint="change")
api.add_resource(OrderFormCheckInResource, '/hotel/orderForm/checkin', endpoint='check_in')
api.add_resource(OrderFormCheckOutResource, '/hotel/orderForm/checkout', endpoint='check_out')
api.add_resource(QueryHotelOrderFormListResource, '/hotel/orderForm/get', endpoint='get_list')
api.add_resource(QueryHotelRoomsInfoResource, '/hotel/room', endpoint="get_all_room")
