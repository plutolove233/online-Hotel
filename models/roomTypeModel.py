# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class RoomType(db.Model):
    __tablename__ = 'room_type'

    AutoID = db.Column(db.BigInteger, primary_key=True, info='自增的主键')
    RoomTypeID = db.Column(db.BigInteger, info='房间种类id')
    HotelID = db.Column(db.BigInteger, info='所属酒店id')
    RoomTypeName = db.Column(db.String(255), info='类型名称')
    Square = db.Column(db.Float(10), info='房间大小')
    Floor = db.Column(db.Integer, info='房间楼层')
    WindowDescription = db.Column(db.String(255), info='房间窗户描述')
    Price = db.Column(db.Float(10), info='房间定价')
    RoomTypeBrief = db.Column(db.String(255), info='房间类型简介')
    RoomPicUrl = db.Column(db.String(255), info='房间类型图片地址')
    IsDeleted = db.Column(db.Integer, server_default=db.FetchedValue(), info='0--未删除，1--删除')
    CreateTime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='创建时间')
