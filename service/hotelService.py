#!/usr/bin/env python
# -*- coding:utf-8 -*-

from controller.hotelController import HotelController
from controller.remarkController import RemarkController
from controller.roomTypeController import RoomTypeController
from utils.response_code import RET,error_map_CN
from app import db
from models.remarkModel import Remark
from models.roomTypeModel import RoomType


class HotelService(HotelController):
    @classmethod
    def get_hotel_details(cls, **kwargs):
        try:
            # hotel = cls.get(HotelID=kwargs.get("HotelID"))
            # if hotel.get("code") != RET.OK:
            #     return hotel
            # remark = RemarkController.get(HotelID=kwargs.get("HotelID"))
            # if remark.get("code") != RET.OK:
            #     return remark
            # roomType = RoomTypeController.get(HotelID=kwargs.get("HotelID"))
            # if roomType.get("code") != RET.OK:
            #     return  roomType
            # res = {
            #     "HotelName": hotel
            # }
            details = db.session.query(cls,Remark,RoomType).filter_by(**kwargs).outer
        except Exception as e:
            return {
                "code": RET.DBERR,
                "data": {
                    "error":str(e),
                },
                "message": error_map_CN(RET.DBERR),
            }
