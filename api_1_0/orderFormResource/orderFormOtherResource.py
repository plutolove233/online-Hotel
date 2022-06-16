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
from service.roomService import RoomService
from utils.myLogging import logger
from utils.response_code import RET
from utils.responseParser import ResponseParser
from utils.generate_id import GenerateID


class GetUserOrderFormInfoResource(Resource):
    @classmethod
    @TokenRequire
    def get(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("HotelID", type=int, location="json", required=False)
        try:
            data = parser.parse_args()
            temp = flask.g.user
            if temp.userType == 1:
                logger.error("user role error")
                return jsonify({
                    "code": RET.ROLEERR,
                    "message": "用户角色错误",
                })
            res = OrderFormService.get_order_form_info(UserID=temp.userId, HotelID=data.get("HotelID"))
            if res.get("code") != RET.OK:
                logger.error(res.get("error"))
                return jsonify(res)

            logger.info("query order form success")
            return jsonify(res)
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
        parser.add_argument("GuestName", type=str, location="form", required=True)
        parser.add_argument("GuestID", type=str, location='form', required=True)
        parser.add_argument("GuestPhone", type=str, location='form', required=True)
        parser.add_argument("ArrivalTime", type=str, location='form', required=True)
        parser.add_argument("CheckOutTime", type=str, location='form', required=True)
        parser.add_argument("HotelID", type=int, location="form", required=True)
        try:
            temp = flask.g.user
            data = parser.parse_args()
            data["ArrivalTime"] = datetime.datetime.strptime(data.get("ArrivalTime"), "%Y-%m-%d %H:%M:%S")
            data["CheckOutTime"] = datetime.datetime.strptime(data.get("CheckOutTime"), "%Y-%m-%d %H:%M:%S")
            data['UserID'] = temp.userId
            query_rooms = RoomService.get(HotelID=data.get("HotelID"), RoomStatus=0)
            if query_rooms.get("code") != RET.OK:
                logger.error(query_rooms.get("data").get("error"))
                return jsonify({
                    "code": query_rooms.get("code"),
                    "error": query_rooms.get("data").get("error"),
                    "message": query_rooms.get("message"),
                })

            if query_rooms.get("totalCount") == 0:
                return jsonify({
                    "code": RET.NODATA,
                    "message": "该房间类型没有空闲",
                })
            # 分配房间
            rooms = query_rooms.get("data")
            data['RoomID'] = rooms[0].get("RoomID")
            data['OrderFormID'] = int(GenerateID.create_random_id())
            # 修改房间状态
            res = RoomService.update(RoomID=data['RoomID'], RoomStatus=1)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": res.get("message"),
                })

            res = OrderFormService.add(**data)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": res.get("message"),
                })
            logger.info("submit order_form success")
            return jsonify({
                "code": RET.OK,
                "message": "提交订单成功",
            })
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


class GetOrderFormListResource(Resource):
    @classmethod
    @TokenRequire
    def get(cls):
        try:
            temp = flask.g.user
            if temp.userType == 1:
                return jsonify(ResponseParser.parse_role_error())
            res = OrderFormService.get_order_list(UserID=temp.userId)
            if res.get("code") != RET.OK:
                logger.error(res.get("error"))
                return jsonify(res)

            logger.info(res.get("message"))
            return jsonify(res)
        except Exception as e:
            logger.warning(str(e))
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))
