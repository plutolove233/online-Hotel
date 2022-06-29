#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:JwtMiddleware.py
# author:刘浩宇
# datetime: 2022/4/23 15:02
# software: PyCharm

"""
This is function description
"""
import jwt.exceptions
from flask import jsonify, g
from flask import request
from utils.jwt import VerifyToken, JWTClaims
from utils.response_code import RET

def TokenRequire(func):
    def innerFunction(*args, **kwargs):
        token = request.headers.get("token")
        try:
            jwtClaim = VerifyToken(token)
        except jwt.exceptions.ExpiredSignatureError:
            return jsonify({
                "codes": RET.LOGINERR,
                "message":"Token已过期",
            })
        except jwt.exceptions.InvalidTokenError:
            return jsonify({
                "codes":RET.PARAMERR,
                "message":"无效Token",
            })
        else:
            user = JWTClaims(userId=jwtClaim.userId,
                             userType=jwtClaim.userType)
            print("token has been auth")
            g.user = user
            return func(*args,**kwargs)
    return innerFunction