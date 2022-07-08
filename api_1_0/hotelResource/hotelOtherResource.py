#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import os

import flask
import werkzeug.datastructures
from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.exceptions import BadRequest
from werkzeug.utils import secure_filename

from service.orderFormService import OrderFormService
from service.roomService import RoomService
from service.roomTypeService import RoomTypeService
from service.userService import UserService
from utils import commons
from utils.calc_time import Calculate
from utils.myLogging import logger
from utils.generate_id import GenerateID
from utils.response_code import RET, error_map_EN
from utils.responseParser import ResponseParser
from service.hotelService import HotelService
from middlewares.JwtMiddleware import TokenRequire


class HotelRegisterResource(Resource):

    @classmethod
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("HotelName", location="json", type=str, required=True, help="HotelName参数类型不正确或缺失")
        parser.add_argument("Phone", location="json", type=str, required=True, help="Phone参数类型不正确或缺失")
        parser.add_argument("Province", location="json", type=str, required=True, help="Province参数类型不正确或缺失")
        parser.add_argument("City", location="json", type=str, required=True, help="City参数类型不正确或缺失")
        parser.add_argument("Area", location="json", type=str, required=True, help="Area参数类型不正确或缺失")
        parser.add_argument("Address", location="json", type=str, required=True, help="Address参数类型不正确或缺失")
        parser.add_argument("HotelAccount", location="json", type=str, required=True, help="HotelAccount参数类型不正确或缺失")
        parser.add_argument("Email", location="json", type=str, required=True, help="Email参数类型不正确或缺失")
        parser.add_argument("Password", location="json", type=str, required=True, help="Password参数类型不正确或缺失")
        try:
            data = parser.parse_args()
            res = HotelService.get(HotelAccount=data.get("HotelAccount"))
            if res.get("code") != RET.OK:
                logger.error(error_map_EN[res.get("code")])
                return jsonify(ResponseParser.parse_res(**res))
            if res.get("totalCount") != 0:
                logger.error(error_map_EN[RET.DATAEXIST])
                return jsonify({
                    "code": RET.DATAEXIST,
                    "error": error_map_EN[RET.DATAEXIST],
                    "message": "该用户信息已注册",
                })

            data['HotelID'] = int(GenerateID.create_random_id())
            data['HotelDist'] = 100.0
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
            return jsonify(ResponseParser.parse_param_error(error=str(e)))
        except Exception as e:
            logger.warning(str(e))
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))


class ChangeHotelInfoResource(Resource):
    @classmethod
    @TokenRequire
    def put(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("HotelName", location="json", type=str, help="HotelName参数类型不正确或缺失")
        parser.add_argument("Province", location="json", type=str, help="Province参数类型不正确或缺失")
        parser.add_argument("City", location="json", type=str, help="City参数类型不正确或缺失")
        parser.add_argument("Area", location="json", type=str, help="Area参数类型不正确或缺失")
        parser.add_argument("Address", location="json", type=str, help="Address参数类型不正确或缺失")
        parser.add_argument("Phone", location="json", type=str, help="Phone参数类型不正确或缺失")
        parser.add_argument("HotelLabels", location="json", type=str, help="HotelLabels参数类型不正确或缺失")
        parser.add_argument("HotelDist", location="json", type=float, help="HotelDist参数类型不正确或缺失")
        parser.add_argument("pic", location="files", type=werkzeug.datastructures.FileStorage)
        try:
            temp = flask.g.user
            if temp.userType == 0:
                return jsonify({
                    "code": RET.ROLEERR,
                    "message": "用户无法访问该功能",
                })
            data = parser.parse_args()

            filename = secure_filename(data.get("pic").filename)
            x = filename.split(".")
            save_name = f"{temp.userId}.{x[-1]}"
            data['HotelPicUrl'] = "http://120.79.200.146:8000/static/hotel/" + save_name
            data.get('pic').save(os.path.join("./static/hotel", save_name))
            # 删除字典pic字段，避免更新时报错
            del data['pic']

            data = commons.put_remove_none(**data)
            res = HotelService.update(HotelID=temp.userId, **data)

            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify(ResponseParser.parse_res(**res))
            logger.info("change hotel info success")
            return jsonify({
                "code": RET.OK,
                "message": "酒店信息修改成功",
            })
        except BadRequest as e:
            logger.error(str(e))
            return jsonify(ResponseParser.parse_param_error(error=str(e)))
        except Exception as e:
            logger.warning(str(e))
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))


class OrderFormCheckInResource(Resource):
    @classmethod
    @TokenRequire
    def put(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("OrderFormID", type=int, location='json', required=True)
        try:
            temp = flask.g.user
            if temp.userType == 0:
                return jsonify(ResponseParser.parse_role_error())

            data = parser.parse_args()
            res = OrderFormService.get(OrderFormID=data.get('OrderFormID'))
            if res.get('code') != RET.OK:
                logger.error(res.get('data').get('error'))
                return jsonify(ResponseParser.parse_res(**res))
            orders = res.get("data")
            userId = orders[0].get("UserID")
            for item in res.get('data'):
                if Calculate.calc_time_diff_days(datetime.datetime.now(), item.get('ArrivalTime')) > 0:
                    return jsonify({
                        "code": RET.REQERR,
                        "message": '未到预定时间',
                    })
            res = OrderFormService.update(OrderFormID=data.get('OrderFormID'), OrderFormStatus=1)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get('error'))
                return jsonify(ResponseParser.parse_res(**res))

            res = UserService.update(UserID=userId, IsInRoom=1)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get('error'))
                return jsonify(ResponseParser.parse_res(**res))

            logger.info('check in success')
            return jsonify(ResponseParser.parse_ok("入住成功", **res.get('data')))
        except BadRequest as e:
            return jsonify(ResponseParser.parse_param_error(error=str(e)))
        except Exception as e:
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))


class OrderFormCheckOutResource(Resource):
    @classmethod
    @TokenRequire
    def put(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("OrderFormID", type=int, location='json', required=True)
        try:
            temp = flask.g.user
            if temp.userType == 0:
                return jsonify(ResponseParser.parse_role_error())

            data = parser.parse_args()

            res = OrderFormService.get(OrderFormID=data.get('OrderFormID'))
            if res.get('code') != RET.OK:
                logger.error(res.get('data').get('error'))
                return jsonify(ResponseParser.parse_res(**res))
            orders = res.get('data')
            userId = orders[0].get('UserID')
            for order in orders:
                res = RoomService.update(RoomID=order.get('RoomID'), RoomStatus=0)
                if res.get('code') != RET.OK:
                    logger.error(res.get('data').get('error'))
                    return jsonify(ResponseParser.parse_res(**res))

            res = OrderFormService.update(OrderFormID=data.get('OrderFormID'), OrderFormStatus=2)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get('error'))
                return jsonify(ResponseParser.parse_res(**res))

            res = UserService.update(UserID=userId, IsInRoom=0)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get('error'))
                return jsonify(ResponseParser.parse_res(**res))

            logger.info('check out success')
            return jsonify(ResponseParser.parse_ok("退房成功", **res.get('data')))
        except BadRequest as e:
            return jsonify(ResponseParser.parse_param_error(error=str(e)))
        except Exception as e:
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))


class QueryHotelOrderFormListResource(Resource):
    @classmethod
    @TokenRequire
    def post(cls):
        temp = flask.g.user
        if temp.userType == 0:
            return jsonify(ResponseParser.parse_role_error())
        parser = reqparse.RequestParser()
        parser.add_argument('OrderFormID', type=int, location='json', required=False)
        try:
            data = parser.parse_args()
            res = OrderFormService.get(**data, HotelID=temp.userId)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify(ResponseParser.parse_res(**res))
            orderList = []
            for item in res.get('data'):
                res = UserService.get(UserID=item.get('UserID'))
                if res.get("code") != RET.OK:
                    logger.error(res.get("data").get("error"))
                    return jsonify(ResponseParser.parse_res(**res))
                user = res.get('data')
                x = {
                    'OrderFormID': item.get('OrderFormID'),
                    'UserName': user[0].get('UserName'),
                    'Phone': user[0].get('Phone'),
                    'FaceUrl': user[0].get('FaceUrl'),
                    'OrderFormStatus': item.get('OrderFormStatus'),
                }
                orderList.append(x)

            logger.info('get order form list success')
            return jsonify(ResponseParser.parse_list_ok('获取宾馆订单信息成功', orderList))
        except Exception as e:
            return ResponseParser.parse_unknown_error(error=str(e))


class QueryHotelRoomsInfoResource(Resource):
    @classmethod
    @TokenRequire
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("RoomNum", type=str, required=False, location="json")
        parser.add_argument("RoomStatus", type=int, required=False, location='json')
        parser.add_argument("RoomTypeName", type=str, required=False, location='json')
        try:
            temp = flask.g.user
            if temp.userType == 0:
                return jsonify(ResponseParser.parse_role_error())
            data = parser.parse_args()
            if data.get("RoomTypeName") is not None:
                res = RoomTypeService.get(RoomTypeName=data.get('RoomTypeName'), HotelID=temp.userId)
                if res.get("code") != RET.OK:
                    logger.error(res.get("data").get("error"))
                    return jsonify(ResponseParser.parse_res(**res))
                roomTypes = res.get("data")
                roomTypeID = roomTypes[0].get("RoomTypeID")
            else:
                roomTypeID = None
            del data['RoomTypeName']
            res = RoomService.get_all(HotelID=temp.userId, RoomTypeID=roomTypeID, **data)
            if res.get("code") != RET.OK:
                logger.error("query all rooms info failed")
                return jsonify(res)

            logger.info("query all rooms info success")
            return jsonify(ResponseParser.parse_list_ok("获取所有房间信息成功", res.get("data")))
        except Exception as e:
            return ResponseParser.parse_unknown_error(error=str(e))
