#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import and_

from controller.roomController import RoomController
from app import db
from models.roomTypeModel import RoomType
from utils import commons
from utils.response_code import RET


class RoomService(RoomController):

    @classmethod
    def get_room_info(cls, **kwargs):
        try:
            room_info = db.session.query(cls.RoomID, cls.RoomNum, cls.RoomStatus, cls.HotelID,
                                         RoomType.RoomTypeID, RoomType.Square, RoomType.Floor,
                                         RoomType.WindowDescription, RoomType.RoomTypeBrief, RoomType.RoomTypeName).filter_by(IsDeleted=0,**kwargs).outerjoin(
                RoomType, and_(
                    RoomType.RoomTypeID == cls.RoomTypeID
                )).all()
            results = commons.query_to_dict(room_info)
            return {
                "code": RET.OK,
                "message": "获取评论信息成功",
                "data": results[0],
            }
        except Exception as e:
            return {
                "code": RET.DBERR,
                "error": str(e),
                "message": "数据库错误"
            }
        finally:
            db.session.close()
