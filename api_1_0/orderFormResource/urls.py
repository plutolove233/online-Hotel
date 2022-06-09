#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import orderform_blueprint
from api_1_0.orderFormResource.orderFormResource import OrderFormResource
from api_1_0.orderFormResource.orderFormOtherResource import GetUserOrderFormResource

api = Api(orderform_blueprint)

api.add_resource(OrderFormResource, '/orderForm/<OrderFormID>', '/orderForm', endpoint='orderForm')
