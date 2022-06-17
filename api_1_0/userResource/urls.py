#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import user_blueprint
from api_1_0.userResource.userResource import UserResource
from api_1_0.userResource.userOtherResource \
    import UserRegisterResource, \
    UserQueryHotelResource, \
    GetHotelDetailsResource, SubmitOrderFormResource, GetOrderFormListResource

api = Api(user_blueprint)

api.add_resource(UserResource, '/user/<UserID>', '/user', endpoint='user')
api.add_resource(UserRegisterResource, "/user/register", endpoint='register')
api.add_resource(UserQueryHotelResource, '/user/query_hotel', endpoint="query_hotel")
api.add_resource(GetHotelDetailsResource, '/user/get_hotel_detail', endpoint="get_detail")
api.add_resource(SubmitOrderFormResource, '/user/orderForm/reserve')
api.add_resource(GetOrderFormListResource, '/user/orderForm/getList', endpoint="getList")
