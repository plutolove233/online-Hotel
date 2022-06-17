#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime

from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.exceptions import BadRequest

from middlewares.JwtMiddleware import TokenRequire
from service.orderFormService import OrderFormService
from service.roomService import RoomService
from utils.calc_time import Calculate
from utils.myLogging import logger
from utils.responseParser import ResponseParser
from utils.response_code import RET


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
            res = OrderFormService.get(OrderFormID=data.get('OrderFormID'))
            if res.get('code') != RET.OK:
                logger.error(res.get('data').get('error'))
                return jsonify(ResponseParser.parse_res(**res))
            orders = res.get('data')
            for order in orders:
                if Calculate.calc_time_diff_days(datetime.datetime.now(), order.get('ArrivalTime')) < 0:
                    return jsonify({
                        "code": RET.INTERNALERR,
                        "message": "订单以逾期",
                    })
                res = RoomService.update(RoomID=order.get('RoomID'), RoomStatus=0)
                if res.get('code') != RET.OK:
                    logger.error(res.get('data').get('error'))
                    return jsonify(ResponseParser.parse_res(**res))
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
