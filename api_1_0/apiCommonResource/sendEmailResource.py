#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:sendEmailResource.py
# author:刘浩宇
# datetime: 2022/6/9 15:25
# software: PyCharm

"""
This is function description
"""

# import module your need
import datetime
from flask import jsonify
from flask_restful import Resource, reqparse

from service.hotelService import HotelService
from service.userService import UserService
from utils import commons
from utils.myLogging import logger
from utils.rsa_encryption_decryption import RSAEncryptionDecryption
from utils.response_code import RET
from utils.SMTP import send_email


class SendEmailResource(Resource):
    @classmethod
    def post(cls):
        global res
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("Phone", location="json", type=str, required=True, help="Phone参数类型不正确或缺失")
            parser.add_argument("UserType", location="json", type=int, required=True, help="UserType参数类型不正确或缺失")
            data = parser.parse_args()
            if data.get('UserType') == 0:
                # --- user ---
                res = UserService.get(Phone=data.get("Phone"))
            elif data.get('UserType') == 1:
                # --- hotel ---
                res = HotelService.get(Phone=data.get("Phone"))
            else:
                logger.error("userType数据错误")
                return jsonify({
                    "code": RET.PARAMERR,
                    "message": "userType数据错误",
                })

            # 处理数据库信息错误
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": res.get("message"),
                })
            # 处理空数据
            if res.get("totalCount") == 0:
                logger.error('user not exist')
                return jsonify({
                    "code": RET.NODATA,
                    "message": "数据不存在",
                })
            # send email
            code = commons.make_verify_code()
            target = res.get("data")
            result = send_email(target[0].get("Email"), code)
            if result.get("code") != RET.OK:
                logger.error(result.get("error"))
                return jsonify({
                    "code": result.get("code"),
                    "error": result.get("error"),
                    "message": "发送邮件失败",
                })

            logger.info("send email success")
            return jsonify({
                "code": RET.OK,
                "message": {
                    "verify_code": RSAEncryptionDecryption.encrypt(code).decode("utf-8"),
                    "send_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            })

        except Exception as e:
            logger.warning(str(e))
            return jsonify({
                "code": RET.UNKOWNERR,
                "error": str(e),
                "message": "未知错误",
            })
