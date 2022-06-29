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
                'OrderFormID': orders[0].get("OrderFormID"),
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
            orders.sort(key=lambda x: x['OrderFormID'])
            group_by_orderForm = []
            for orderFormID, items in groupby(orders, key=itemgetter('OrderFormID')):
                items = list(items)
                # print(items)
                res = HotelController.get(HotelID=items[0].get('HotelID'))
                if res.get("code") != RET.OK:
                    return ResponseParser.parse_db_error(error=res.get("data").get("error"))
                if res.get("totalCount") == 0:
                    continue
                hotel = res.get("data")
                data = {
                    'OrderFormID': orderFormID,
                    "HotelID": hotel[0].get("HotelID"),
                    "HotelName": hotel[0].get("HotelName"),
                    "HotelPicUrl": hotel[0].get("HotelPicUrl"),
                    "ArrivalTime": items[0].get("ArrivalTime"),
                    "OrderFormStatus": items[0].get("OrderFormStatus"),
                    "totalCount": len(items),
                    "price": cls.calc_order_form_cost(OrderFormID=orderFormID).get("data").get(
                        "price")
                }
                group_by_orderForm.append(data)
            return ResponseParser.parse_list_ok("获取订单列表成功", group_by_orderForm)
        except Exception as e:
            return ResponseParser.parse_unknown_error(error=str(e))

    @classmethod
    def calc_order_form_cost(cls, **kwargs):
        try:
            orderFormID = kwargs.get("OrderFormID")
            res = cls.get(OrderFormID=orderFormID)
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
