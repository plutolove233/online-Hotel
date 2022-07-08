#!/usr/bin/env python
# -*- coding:utf-8 -*-

import flask
from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.exceptions import BadRequest

from middlewares.JwtMiddleware import TokenRequire
from service.roomService import RoomService
from utils.myLogging import logger
from utils.responseParser import ResponseParser
from utils.response_code import RET
from utils.generate_id import GenerateID


class AddRoomResource(Resource):
    @classmethod
    @TokenRequire
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("RoomNum", location="json", type=str, required=True)
        parser.add_argument("RoomTypeID", location="json", type=int, required=True)
        try:
            temp = flask.g.user
            if temp.userType == 0:
                return jsonify({
                    "code": RET.ROLEERR,
                    "message": "用户无法访问此功能",
                })

            data = parser.parse_args()
            data['RoomID'] = int(GenerateID.create_random_id())
            data['HotelID'] = temp.userId

            res = RoomService.add(**data)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": res.get("message")
                })

            logger.info("add room success")
            return jsonify({
                "code": RET.OK,
                "message": "添加房间信息成功",
                "data": data,
            })

        except BadRequest as e:
            logger.error(str(e))
            return jsonify({
                "code": RET.PARAMERR,
                "error": str(e),
                "message": "获取请求参数失败"
            })


class GetRoomInfoResource(Resource):
    @classmethod
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("RoomID", type=int, location="json", required=True)
        try:
            data = parser.parse_args()
            res = RoomService.get_room_info(**data)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": res.get("message")
                })

            logger.info("query room infomation success")
            return jsonify(res)
        except BadRequest as e:
            logger.error(str(e))
            return jsonify(ResponseParser.parse_param_error(error=str(e)))
        except Exception as e:
            logger.warning(str(e))
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))
