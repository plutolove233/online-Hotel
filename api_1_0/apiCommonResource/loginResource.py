#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:loginResource.py
# author:刘浩宇
# datetime: 2022/6/5 15:24
# software: PyCharm

"""
This is function description
"""

from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.exceptions import BadRequest

from service.hotelService import HotelService
from utils.response_code import RET, error_map_EN
from utils.myLogging import logger
from utils.jwt import MakeToken
from utils.responseParser import ResponseParser
from utils.rsa_encryption_decryption import RSAEncryptionDecryption
from service.userService import UserService


class LoginResource(Resource):

    @classmethod
    def post(cls):
        global res
        parser = reqparse.RequestParser()
        parser.add_argument("account", type=str, location='json', required=True, help="account参数类型不正确或缺失")
        parser.add_argument("userType", type=int, location="json", required=True, help="userType参数类型不正确或缺失")
        parser.add_argument("password", type=str, location="json", required=True, help="password参数类型不正确或缺失")
        try:
            data = parser.parse_args()
            if data.get("userType") == 0:
                # 0--住客用户登录
                kwargs = {
                    "Phone": data.get("account"),
                }
                res = UserService.get(**kwargs)

            elif data.get("userType") == 1:
                # 1---宾馆账号登录
                kwargs = {
                    "HotelAccount": data.get("account"),
                }
                res = HotelService.get(**kwargs)
            else:
                logger.error('userType值不正确')
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify(ResponseParser.parse_res(**res))
            if res.get("totalCount") == 0:
                logger.error("user not register")
                return jsonify(ResponseParser.parse_no_data(message="用户未注册"))
            user = res.get("data")
            cipher = user[0].get('Password')
            plain = RSAEncryptionDecryption.decrypt(cipher_text=cipher).encode('utf-8').decode()
            if plain == data.get("password"):
                logger.info('login success')
                id = user[0].get("UserID") if data.get("userType") ==0 else user[0].get("HotelID")
                return jsonify({
                    "code": RET.OK,
                    "message": "登录成功",
                    "data": {
                        "user": user[0],
                        "token": MakeToken(userId=id, userType=data.get("userType")),
                    }
                })
            else:
                logger.error('log in failed')
                return jsonify({
                    "code": RET.PWDERR,
                    "error": error_map_EN[RET.PWDERR],
                    "message": "登录失败",
                })

        except BadRequest as e:
            logger.error(str(e))
            return jsonify(ResponseParser.parse_param_error(error=str(e)))
        except Exception as e:
            logger.warning(str(e))
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))
