#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import orderform_blueprint
from api_1_0.orderFormResource.orderFormResource import OrderFormResource
from api_1_0.orderFormResource.orderFormOtherResource import GetUserOrderFormInfoResource, SubmitOrderFormResource

api = Api(orderform_blueprint)

api.add_resource(OrderFormResource, '/orderForm/<OrderFormID>', '/orderForm', endpoint='orderForm')
api.add_resource(GetUserOrderFormInfoResource, '/orderForm/getOrderInfo', endpoint="getInfo")
api.add_resource(SubmitOrderFormResource, '/orderForm/reserve')