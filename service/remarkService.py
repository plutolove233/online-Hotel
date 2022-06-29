#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import and_

from controller.remarkController import RemarkController
from app import db
from models.userModel import User
from utils import commons
from utils.response_code import RET


class RemarkService(RemarkController):
    
    @classmethod
    def GetHotelRemark(cls, **kwargs):
        try:
            remark_info = db.session.query(cls.RemarkID, cls.RemarkContent, cls.CreateTime, User.UserID, User.UserName, User.FaceUrl).filter_by(IsDeleted=0,**kwargs).outerjoin(User, and_(
                User.UserID == cls.RemarkUserID
            )).all()
            results = commons.query_to_dict(remark_info)
            results.sort(key=lambda x:x['CreateTime'], reverse=True)
            return {
                "code": RET.OK,
                "message":"获取评论信息成功",
                "data": results,
            }
        except Exception as e:
            return {
                "code": RET.DBERR,
                "error": str(e),
                "message": "数据库错误"
            }
        finally:
            db.session.close()

