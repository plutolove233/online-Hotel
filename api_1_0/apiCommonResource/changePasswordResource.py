#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:changePasswordResource.py
# author:刘浩宇
# datetime: 2022/6/10 16:47
# software: PyCharm

"""
This is function description
"""

from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.exceptions import BadRequest

from service.hotelService import HotelService
from service.userService import UserService
from utils.myLogging import logger
from utils.response_code import RET
from utils.responseParser import ResponseParser


class ChangePwdResource(Resource):
    @classmethod
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("Phone", location="json", type=str, required=True, help="Phone参数类型不正确或缺失")
        parser.add_argument("VerifyCode", location="json", type=str, required=True, help="Verify参数类型不正确或缺失")
        parser.add_argument("Password", location="json", type=str, required=True, help="Password参数类型不正确或缺失")
        parser.add_argument("UserType", location="json", type=int, required=True, help="UserType参数类型不正确或缺失")
        try:
            global res
            data = parser.parse_args()
            if data.get("UserType") == 0:
                # --- user ---
                res = UserService.get(Phone=data.get("Phone"))
            elif data.get("UserType") == 1:
                # --- hotel ---
                res = HotelService.get(Phone=data.get("Phone"))
            else:
                logger.error("userType value is wrong")
                return jsonify(ResponseParser.parse_res(**res))

            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify(ResponseParser.parse_res(**res))
            if res.get("totalCount") == 0:
                logger.error('user not exist')
                return jsonify(ResponseParser.parse_no_data(message='用户信息不存在'))
            user = res.get("data")
            if data.get("UserType") == 0:
                # --- user ---
                result = UserService.update(UserID=user[0].get("UserID"), Password=data.get("Password"))
            else:
                # --- hotel ---
                result = HotelService.update(HotelID=user[0].get("HotelID"), Password=data.get("Password"))
            if result.get("code") != RET.OK:
                logger.error(result.get("data").get("error"))
                return jsonify(ResponseParser.parse_res(**res))

            logger.info("change password success")
            return jsonify(ResponseParser.parse_ok("密码修改成功"))
        except BadRequest as e:
            logger.error(str(e))
            return jsonify(ResponseParser.parse_param_error(error=str(e)))
        except Exception as e:
            logger.warning(str(e))
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))
