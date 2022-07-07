#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import datetime

import flask
import werkzeug.datastructures
from flask_restful import reqparse, Resource
from flask import jsonify
from werkzeug.exceptions import BadRequest
from werkzeug.utils import secure_filename

from middlewares.JwtMiddleware import TokenRequire
from service.hotelService import HotelService
from service.orderFormService import OrderFormService
from service.roomService import RoomService
from service.roomTypeService import RoomTypeService
from utils import commons
from utils.commons import put_remove_none
from utils.generate_id import GenerateID
from service.userService import UserService
from utils.myLogging import logger
from utils.responseParser import ResponseParser
from utils.response_code import RET, error_map_EN


class UserRegisterResource(Resource):
    @classmethod
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('UserName', location='form', required=True, type=str, help='UserName参数类型不正确或缺失')
        parser.add_argument('Password', location='form', required=True, type=str, help='Password参数类型不正确或缺失')
        parser.add_argument('Phone', location='form', required=True, type=str, help='Phone参数类型不正确或缺失')
        parser.add_argument('Email', location='form', required=True, type=str, help='Email参数类型不正确或缺失')
        parser.add_argument("pic", location="files", type=werkzeug.datastructures.FileStorage, required=False)
        try:
            kwargs = parser.parse_args()

            res = UserService.get(Phone=kwargs.get("Phone"))
            if res.get("code") != RET.OK:
                logger.error(error_map_EN[res.get("code")])
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": res.get("message"),
                })
            if res.get("totalCount") != 0:
                logger.error(error_map_EN[RET.DATAEXIST])
                return jsonify({
                    "code": RET.DATAEXIST,
                    "error": error_map_EN[RET.DATAEXIST],
                    "message": "用户手机信息已注册",
                })

            kwargs['UserID'] = int(GenerateID.create_random_id())

            if kwargs.get("pic") is not None:
                filename = secure_filename(kwargs.get("pic").filename)
                x = filename.split(".")
                save_name = f"{kwargs.get('UserID')}.{x[-1]}"
                kwargs['FaceUrl'] = "http://api.onlineHotel.com/static/user/" + save_name
                kwargs.get('pic').save(os.path.join("./static/user", save_name))
            # 删除字典pic字段，避免更新时报错
            else:
                kwargs['FaceUrl'] = 'http://api.onlineHotel.com/static/user/default.jpg'
            del kwargs['pic']

            kwargs = commons.put_remove_none(**kwargs)
            res = UserService.add(**kwargs)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": "用户注册失败",
                })
            logger.info(f"user {kwargs['UserID']} register success")
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


class UserQueryHotelResource(Resource):
    @classmethod
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("Province", location="form", required=True, type=str, help="Province参数类型不正确或缺失")
        parser.add_argument("City", location="form", required=True, type=str, help="City参数类型不正确或缺失")
        parser.add_argument("Area", location="form", type=str, required=True, help="Area参数类型不正确或缺失")
        try:
            kwargs = parser.parse_args()
            kwargs = put_remove_none(**kwargs)

            res = HotelService.get(**kwargs)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": res.get("message"),
                })

            for item in res.get('data'):
                result = RoomTypeService.get(HotelID=item.get('HotelID'))
                if result.get("code") != RET.OK:
                    logger.error(result.get('data').get('error'))
                    return jsonify(ResponseParser.parse_res(**result))
                if result.get("totalCount") == 0:
                    del item
                    continue
                roomType = result.get('data')
                roomType.sort(key=lambda x: x['Price'])

            dataParser = ['Province', 'City', 'Area', 'HotelID', 'HotelName', 'Phone', 'HotelLabels', 'HotelDist',
                          'HotelPicUrl']
            data = commons.data_screen_by_list(res.get("data"), dataParser)

            logger.info(f"query {kwargs.get('Province')}-{kwargs.get('City')}-{kwargs.get('Area')} success")
            return jsonify({
                "code": RET.OK,
                "message": "查询成功",
                "data": data,
            })
        except BadRequest as e:
            logger.error(str(e))
            return jsonify(ResponseParser.parse_param_error(error=str(e)))
        except Exception as e:
            logger.warning(str(e))
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))


class GetHotelDetailsResource(Resource):
    @classmethod
    def get(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("HotelID", location="json", type=int, required=True)
        try:
            data = parser.parse_args()
            res = HotelService.get_hotel_details(**data)
            if res.get("code") != RET.OK:
                logger.error(res.get("data").get("error"))
                return jsonify({
                    "code": res.get("code"),
                    "error": res.get("data").get("error"),
                    "message": res.get("message"),
                })

            logger.info("query hotel detail success")
            return jsonify(res)
        except BadRequest as e:
            logger.error(str(e))
            return jsonify(ResponseParser.parse_param_error(error=str(e)))
        except Exception as e:
            logger.warning(str(e))
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))


class SubmitOrderFormResource(Resource):
    @classmethod
    @TokenRequire
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("GuestName", type=str, location="form", required=True)
        parser.add_argument("GuestID", type=str, location='form', required=True)
        parser.add_argument("GuestPhone", type=str, location='form', required=True)
        parser.add_argument("ArrivalTime", type=str, location='form', required=True)
        parser.add_argument("CheckOutTime", type=str, location='form', required=True)
        parser.add_argument("HotelID", type=int, location="form", required=True)
        parser.add_argument("RoomTypeID", type=int, location='form', required=True)
        try:
            temp = flask.g.user
            data = parser.parse_args()
            data["ArrivalTime"] = datetime.datetime.strptime(data.get("ArrivalTime"), "%Y-%m-%d")
            data["CheckOutTime"] = datetime.datetime.strptime(data.get("CheckOutTime"), "%Y-%m-%d")
            query_rooms = RoomService.get(HotelID=data.get("HotelID"), RoomStatus=0, RoomTypeID=data.get('RoomTypeID'))
            if query_rooms.get("code") != RET.OK:
                logger.error(query_rooms.get("data").get("error"))
                return jsonify({
                    "code": query_rooms.get("code"),
                    "error": query_rooms.get("data").get("error"),
                    "message": query_rooms.get("message"),
                })

            guests = data.get('GuestID')
            phones = data.get('GuestPhone')
            names = data.get('GuestName')
            guests = guests.split('/')
            phones = phones.split('/')
            names = names.split('/')

            if query_rooms.get("totalCount") < len(guests):
                return jsonify({
                    "code": RET.NODATA,
                    "message": "该房间类型数量不够",
                })

            rooms = query_rooms.get("data")

            orderFormID = int(GenerateID.create_random_id())
            order = {
                'UserID': temp.userId,
                'HotelID': data.get('HotelID'),
                'ArrivalTime': data.get('ArrivalTime'),
                'CheckOutTime': data.get('CheckOutTime'),
            }
            for index, guest in enumerate(guests):
                # 分配房间
                order['RoomID'] = rooms[index].get("RoomID")
                order['OrderFormID'] = orderFormID
                order['GuestID'] = guest
                order['GuestName'] = names[index]
                order['GuestPhone'] = phones[index]

                # 修改房间状态
                res = RoomService.update(RoomID=order['RoomID'], RoomStatus=1)
                if res.get("code") != RET.OK:
                    logger.error(res.get("data").get("error"))
                    return jsonify(ResponseParser.parse_res(**res))

                res = OrderFormService.add(**order)
                if res.get("code") != RET.OK:
                    logger.error(res.get("data").get("error"))
                    return jsonify(ResponseParser.parse_res(**res))
            logger.info("submit order_form success")
            return jsonify({
                "code": RET.OK,
                "message": "提交订单成功",
            })
        except BadRequest as e:
            logger.error(str(e))
            return jsonify(ResponseParser.parse_param_error(error=str(e)))
        except Exception as e:
            logger.warning(str(e))
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))


class GetOrderFormListResource(Resource):
    @classmethod
    @TokenRequire
    def get(cls):
        try:
            temp = flask.g.user
            if temp.userType == 1:
                return jsonify(ResponseParser.parse_role_error())
            res = OrderFormService.get_order_list(UserID=temp.userId)
            if res.get("code") != RET.OK:
                logger.error(res.get("error"))
                return jsonify(res)

            logger.info(res.get("message"))
            return jsonify(res)
        except Exception as e:
            logger.warning(str(e))
            return jsonify(ResponseParser.parse_unknown_error(error=str(e)))
