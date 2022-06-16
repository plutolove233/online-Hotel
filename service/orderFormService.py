#!/usr/bin/env python
# -*- coding:utf-8 -*-
from itertools import groupby
from operator import itemgetter

from controller.hotelController import HotelController
from controller.orderFormController import OrderFormController
from controller.roomController import RoomController
from controller.roomTypeController import RoomTypeController
from utils import commons
from utils.responseParser import ResponseParser
from utils.response_code import RET


class OrderFormService(OrderFormController):

    @classmethod
    def get_order_form_info(cls, **kwargs):
        kwargs = commons.put_remove_none(**kwargs)
        try:
            res = cls.get(**kwargs)
            if res.get("code") != RET.OK:
                return ResponseParser.parse_res(**res)
            if res.get("totalCount") == 0:
                return ResponseParser.parse_no_data(message="订单信息为空")
            orders = res.get("data")
            price = 0
            data = {
                'OrderFormID': [],
                'EACH_ROOM_INFO': [],
                'ArrivalTime': orders[0].get("ArrivalTime"),
                'CheckOutTime': orders[0].get("CheckOutTime")
            }
            for item in orders:

                res = RoomController.get(RoomID=item.get("RoomID"))
                if res.get("code") != RET.OK:
                    return ResponseParser.parse_res(**res)
                if res.get("totalCount") == 0:
                    continue

                room = res.get("data")
                item['RoomNum'] = room[0].get("RoomNum")

                res = RoomTypeController.get(RoomTypeID=room[0].get('RoomTypeID'))
                if res.get("code") != RET.OK:
                    return ResponseParser.parse_res(**res)
                if res.get("totalCount") == 0:
                    continue

                room_type = res.get("data")
                price += room_type[0].get("Price")
                data['OrderFormID'].append(item.get("OrderFormID"))
                data['EACH_ROOM_INFO'].append(item)
            data['Price'] = price
            return ResponseParser.parse_ok("获取订单信息成功", **data)
        except Exception as e:
            return ResponseParser.parse_unknown_error(error=str(e))

    @classmethod
    def get_order_list(cls, **kwargs):
        try:
            res = cls.get(UserID=kwargs.get("UserID"))
            if res.get("code") != RET.OK:
                return ResponseParser.parse_db_error(error=res.get("data").get("error"))
            orders = res.get('data')
            orders.sort(key=lambda x: x['HotelID'])
            group_by_hotel = []
            for hotelID, items in groupby(orders, key=itemgetter('HotelID')):
                items = list(items)
                res = HotelController.get(HotelID=hotelID)
                if res.get("code") != RET.OK:
                    return ResponseParser.parse_db_error(error=res.get("data").get("error"))
                if res.get("totalCount") == 0:
                    continue
                hotel = res.get("data")
                data = {
                    "HotelID": hotel[0].get("HotelID"),
                    "HotelName": hotel[0].get("HotelName"),
                    "HotelPicUrl": hotel[0].get("HotelPicUrl"),
                    "ArrivalTime": items[0].get("ArrivalTime"),
                    "OrderFormStatus": items[0].get("OrderFormStatus"),
                    "totalCount": len(items),
                    "price": cls.calc_user_cost(UserID=kwargs.get("UserID"), HotelID=hotelID).get("data").get(
                        "price")
                }
                group_by_hotel.append(data)
            return ResponseParser.parse_list_ok("获取订单列表成功", group_by_hotel)
        except Exception as e:
            return ResponseParser.parse_unknown_error(error=str(e))

    @classmethod
    def calc_user_cost(cls, **kwargs):
        try:
            userID = kwargs.get("UserID")
            hotelID = kwargs.get("HotelID")
            res = cls.get(UserID=userID, HotelID=hotelID)
            if res.get("code") != RET.OK:
                return ResponseParser.parse_db_error(error=res.get("data").get("error"))
            orders = res.get("data")
            price = 0
            for item in orders:
                res = RoomController.get(RoomID=item.get("RoomID"))
                if res.get("code") != RET.OK:
                    return ResponseParser.parse_db_error(error=res.get("data").get("error"))
                if res.get("totalCount") == 0:
                    continue
                room = res.get("data")
                res = RoomTypeController.get(RoomTypeID=room[0].get("RoomType"))
                if res.get("code") != RET.OK:
                    return ResponseParser.parse_db_error(error=res.get("data").get("error"))
                if res.get("totalCount") == 0:
                    continue
                roomType = res.get("data")
                price += roomType[0].get("Price")
            return ResponseParser.parse_ok("获取用户订单价格成功", price=price)
        except Exception as e:
            return ResponseParser.parse_unknown_error(error=str(e))
