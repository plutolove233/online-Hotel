#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

import flask
import werkzeug.datastructures
from flask import jsonify
from flask_restful import Resource, reqparse, request
from werkzeug.exceptions import BadRequest
from werkzeug.utils import secure_filename

from middlewares.JwtMiddleware import TokenRequire
from service.roomTypeService import RoomTypeService
from utils.myLogging import logger
from utils.responseParser import ResponseParser
from utils.response_code import RET
from utils import commons
from utils.generate_id import GenerateID


class AddRoomTypeResource(Resource):
    @classmethod
    @TokenRequire
    def post(cls):
        temp = flask.g.user
        if temp.userType == 0:
            return jsonify({
                "code": RET.ROLEERR,
                "message": "用户无法访问该功能",
            })
        parser = reqparse.RequestParser()
        parser.add_argument("RoomTypeName", location="json", type=str, required=True)
        parser.add_argument("Square", location="json", type=float, required=True)
        parser.add_argument("Floor", location="json", type=int, required=True)
        parser.add_argument("WindowDescription", location="json", type=str, required=True)
        parser.add_argument("Price", location="json", type=float, required=True)
        parser.add_argument("RoomTypeBrief", location="json", type=str, required=True)
        parser.add_argument("pic", location="files", type=werkzeug.datastructures.FileStorage, required=True)
        try:
            data = parser.parse_args()
            data["RoomTypeID"] = int(GenerateID.create_random_id())

            filename = secure_filename(data.get("pic").filename)
            x = filename.split(".")
            save_name = f"{data['RoomTypeID']}.{x[-1]}"
            data['RoomPicUrl'] = "http://api.onlineHotel.com/static/roomType/" + save_name
            data.get("pic").save(os.path.join("./static/roomType", save_name))
            del data['pic']

            data['HotelID'] = temp.userId
            data = commons.put_remove_none(**data)
            res = RoomTypeService.add(**data)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": res.get("message"),
                })
            logger.info("add room  type success")
            return jsonify({
                "code": RET.OK,
                "message": "房间类型添加成功",
                "data": data,
            })
        except BadRequest as e:
            logger.error(str(e))
            return jsonify(ResponseParser.parse_param_error(error=str(e)))
        except Exception as e:
            logger.warning(str(e))
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))