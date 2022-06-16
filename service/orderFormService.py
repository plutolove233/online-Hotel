#!/usr/bin/env python
# -*- coding:utf-8 -*-

from controller.orderFormController import OrderFormController
from controller.roomController import RoomController
from controller.roomTypeController import RoomTypeController
from utils import commons
from utils.response_code import RET, error_map_CN
from utils.responseParser import ResponseParser


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
                    return ResponseParser.parse_no_data(message="房间信息为空")

                room = res.get("data")
                item['RoomNum'] = room[0].get("RoomNum")

                res = RoomTypeController.get(RoomTypeID=room[0].get('RoomTypeID'))
                if res.get("code") != RET.OK:
                    return ResponseParser.parse_res(**res)
                if res.get("totalCount") == 0:
                    return ResponseParser.parse_no_data(message="房间类型信息为空")

                room_type = res.get("data")
                price += room_type[0].get("Price")
                data['OrderFormID'].append(item.get("OrderFormID"))
                data['EACH_ROOM_INFO'].append(item)
            data['Price'] = price
            return ResponseParser.parse_ok("获取订单信息成功",**data)
        except Exception as e:
            return {
                "code": RET.DBERR,
                "error": str(e),
                "message": error_map_CN[RET.DBERR]
            }
