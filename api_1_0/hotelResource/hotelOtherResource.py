#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.exceptions import BadRequest

from utils import commons
from utils.myLogging import logger
from utils.generate_id import GenerateID
from utils.response_code import RET, error_map_EN
from service.hotelService import HotelService


class HotelRegisterResource(Resource):

    @classmethod
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("HotelName", location="form", type=str, required=True, help="HotelName参数类型不正确或缺失")
        parser.add_argument("Phone", location="form", type=str, required=True, help="Phone参数类型不正确或缺失")
        parser.add_argument("Province", location="form", type=str, required=True, help="Province参数类型不正确或缺失")
        parser.add_argument("City", location="form", type=str, required=True, help="City参数类型不正确或缺失")
        parser.add_argument("Area", location="form", type=str, required=True, help="Area参数类型不正确或缺失")
        parser.add_argument("HotelAccount", location="form", type=str, required=True, help="HotelAccount参数类型不正确或缺失")
        parser.add_argument("Email", location="form", type=str, required=True, help="Email参数类型不正确或缺失")
        parser.add_argument("Password", location="form", type=str, required=True, help="Password参数类型不正确或缺失")
        try:
            data = parser.parse_args()
            res = HotelService.get(Phone=data.get("Phone"))
            if res.get("code") != RET.OK:
                logger.error(error_map_EN(res.get("code")))
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": res.get("message"),
                })

            if res.get("totalCount") != 0:
                logger.error(error_map_EN(RET.DATAEXIST))
                return jsonify({
                    "code": RET.DATAEXIST,
                    "error": error_map_EN(RET.DATAEXIST),
                    "message": "该用户信息已注册",
                })

            data['HotelID'] = int(GenerateID.create_random_id())
            data = commons.put_remove_none(**data)
            res = HotelService.add(**data)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": "用户注册失败",
                })
            logger.info(f"hotel {data['HotelID']} register success")
            return jsonify({
                "code": RET.OK,
                "message": "用户注册成功",
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
                "code": RET.UNKOWNERR,
                "error": str(e),
                "message": "未知错误",
            })
