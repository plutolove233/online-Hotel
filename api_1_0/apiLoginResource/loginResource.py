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

from utils.response_code import RET, error_map_EN
from utils.loggings import loggings
from utils.jwt import MakeToken
from utils.rsa_encryption_decryption import RSAEncryptionDecryption
from service.userService import UserService


class LoginResource(Resource):

    @classmethod
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("account", type=str, location='form', required=True, help="account参数类型不正确或缺失")
        parser.add_argument("userType", type=int, location="form", required=True, help="userType参数类型不正确或缺失")
        parser.add_argument("password", type=str, location="form", required=True, help="password参数类型不正确或缺失")
        try:
            data = parser.parse_args()
            # print(data)
            if data.get("userType") == 0:
                # 0--住客用户登录
                kwargs = {
                    "Phone": data.get("account"),
                }
                res = UserService.get(**kwargs)
                if res.get("code") != RET.OK:
                    return jsonify({
                        "code": res.get("code"),
                        "error": res.get("data").get("error"),
                        "message": res.get("message"),
                    })
                user = res.get("data")
                cipher = user[0].get('Password')
                plain = RSAEncryptionDecryption.decrypt(cipher_text=cipher).encode('utf-8').decode()
                if plain == data.get("password"):
                    return jsonify({
                        "code": RET.OK,
                        "message": "登录成功",
                        "data": {
                            "user": user[0],
                            "token":MakeToken(userId=user[0].get("UserID"), userType=0),
                        }
                    })
                else:
                    return jsonify({
                        "code": RET.PWDERR,
                        "error": error_map_EN[RET.PWDERR],
                        "message": "登录失败",
                    })

            elif data.get("userType") == 1:
                pass
        except BadRequest as e:
            return jsonify({
                "code": RET.PARAMERR,
                "error": str(e),
                "message": "获取请求参数失败",
            })
        except Exception as e:
            return jsonify({
                "code": RET.UNKOWNERR,
                "error": str(e),
                "message": "未知错误",
            })
