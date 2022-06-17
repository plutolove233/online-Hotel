#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime

from werkzeug.exceptions import BadRequest
from flask_restful import Resource, reqparse
import flask
from flask import jsonify

from middlewares.JwtMiddleware import TokenRequire
from service.orderFormService import OrderFormService
from utils.myLogging import logger
from utils.response_code import RET
from utils.responseParser import ResponseParser


class GetUserOrderFormInfoResource(Resource):
    @classmethod
    @TokenRequire
    def get(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('OrderFormID', type=int, location='json', required=True)
        try:
            data = parser.parse_args()
            res = OrderFormService.get_order_form_info(**data)
            if res.get("code") != RET.OK:
                logger.error(res.get("error"))
                return jsonify(res)

            logger.info("query order form success")
            return jsonify(res)

        except Exception as e:
            logger.warning(str(e))
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))


class CancelOrderFormResource(Resource):
    @classmethod
    @TokenRequire
    def put(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('OrderFormID', type=int, location='json', required=True)
        try:
            data = parser.parse_args()
            res = OrderFormService.delete(OrderFormID=data.get('OrderFormID'))
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify(ResponseParser.parse_res(**res))

            logger.info('cancel order success')
            return jsonify(ResponseParser.parse_ok("订单取消成功"), **res.get("data"))
        except BadRequest as e:
            return jsonify(ResponseParser.parse_param_error(error=str(e)))
        except Exception as e:
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))


