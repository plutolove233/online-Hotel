#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import and_

from controller.hotelController import HotelController
from controller.roomTypeController import RoomTypeController
from service.remarkService import RemarkService
from utils import commons
from utils.response_code import RET,error_map_CN


class HotelService(HotelController):
    @classmethod
    def get_hotel_details(cls, **kwargs):
        try:
            hotel = cls.get(HotelID=kwargs.get("HotelID"))
            if hotel.get("code") != RET.OK:
                return hotel
            screener = ['HotelID', 'HotelName', 'Phone', 'Province', 'City', 'Area', 'Address', 'HotelPicUrl', 'HotelLabels']
            hotel = hotel.get("data")
            hotel = commons.data_screen_by_list(hotel, screener)
            remark = RemarkService.GetHotelRemark(HotelID=kwargs.get("HotelID"))
            if remark.get("code") != RET.OK:
                return remark
            remark = remark.get("data")
            screener = ['RemarkID', 'RemarkContent', 'UserName', 'FaceUrl', 'CreateTime']
            remark = commons.data_screen_by_list(remark, screener)
            roomType = RoomTypeController.get(HotelID=kwargs.get("HotelID"))
            if roomType.get("code") != RET.OK:
                return roomType
            res = {
                "Hotel": hotel[0],
                "Remark": remark[0],
                "RoomType": roomType.get("data"),
            }
            return {
                "code": RET.OK,
                "message":"查询成功",
                "data":res
            }
        except Exception as e:
            return {
                "code": RET.DBERR,
                "data": {
                    "error":str(e),
                },
                "message": error_map_CN(RET.DBERR),
            }
