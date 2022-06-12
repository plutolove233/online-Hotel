#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime

import werkzeug.datastructures
from flask_restful import Resource, reqparse
import flask
from flask import jsonify
from werkzeug.exceptions import BadRequest

from middlewares.JwtMiddleware import TokenRequire
from service.orderFormService import OrderFormService
from utils.myLogging import logger
from utils.response_code import RET


class GetUserOrderFormResource(Resource):
    @classmethod
    @TokenRequire
    def get(cls):
        try:
            temp = flask.g.user
            if temp.userType == 1:
                logger.error("user role error")
                return jsonify({
                    "code": RET.ROLEERR,
                    "message": "用户角色错误",
                })
            res = OrderFormService.get(UserID=temp.userId)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": res.get("message"),
                })

            """waiting to complete"""

            logger.info("query order form success")
            return jsonify({
                "code": RET.OK,
                "message": res.get("data"),
            })
        except Exception as e:
            logger.warning(str(e))
            return jsonify({
                "code": RET.PARAMERR,
                "error": str(e),
                "message": "请求参数缺失"
            })


class SubmitOrderFormResource(Resource):
    @classmethod
    @TokenRequire
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("GuestName", type=str, location="json", required=True)
        parser.add_argument("GuestID", type=str, location='json', required=True)
        parser.add_argument("GuestPhone", type=str, location='json', required=True)
        parser.add_argument("ArrivalTime",  location='json', required=True)
        parser.add_argument("CheckOutTime", location='json', required=True)
        try:
            temp = flask.g.user
            data = parser.parse_args()
            print(type(data.get("ArrivalTime")))
        except BadRequest as e:
            logger.error(str(e))
            return jsonify({
                "code": RET.PARAMERR,
                "error": str(e),
                "message": "获取请求参数失败",
            })
        except Exception as e:
            logger.warning(str(e))
            return jsonify({
                "code": RET.PARAMERR,
                "error": str(e),
                "message": "请求参数缺失"
            })
