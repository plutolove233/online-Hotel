#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Resource, reqparse
import flask
from flask import jsonify
from werkzeug.exceptions import BadRequest

from middlewares.JwtMiddleware import TokenRequire
from service.orderFormService import OrderFormService
from utils.myLogging import logger
from utils.response_code import RET


class GetUserOrderFormResource(Resource):
    @classmethod
    @TokenRequire
    def get(cls):
        try:
            temp = flask.g.user
            if temp.userType == 1:
                logger.error("user role error")
                return jsonify({
                    "code": RET.ROLEERR,
                    "message": "用户角色错误",
                })
            res = OrderFormService.get(UserID=temp.userId)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": res.get("message"),
                })

            """waiting to complete"""
            logger.info("query order form success")
            return jsonify({
                "code": RET.OK,
                "message": res.get("data"),
            })
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
        pass
