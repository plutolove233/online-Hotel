#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:jwt.py
# author:刘浩宇
# datetime: 2022/4/23 15:15
# software: PyCharm

"""
This is function description
"""

import jwt
from datetime import datetime, timedelta
from app.setting import site


class JWTClaims():
    def __init__(self, userId, userType):
        self.userId = userId
        self.userType = userType


def genToken(claim: JWTClaims):
    payload = {
        "exp": datetime.now() + timedelta(seconds=int(site.CONFIG['BASIC']['token_expires'])),
        'userID': claim.userId,
        "userType": claim.userType,
    }
    encoded_jwt = jwt.encode(payload, site.CONFIG['BASIC']['secret_key'], algorithm='HS256')
    return encoded_jwt


def MakeToken(userId: int, userType: int) -> str:
    claim = JWTClaims(userId=userId,
                      userType=userType)
    return genToken(claim)


def VerifyToken(strToken:str)->JWTClaims:
    token = jwt.decode(strToken, site.CONFIG['BASIC']['secret_key'], algorithms="HS256")
    claim = JWTClaims(userId=token['userID'],
                      userType=token['userType'])
    return claim
