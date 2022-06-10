# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Room(db.Model):
    __tablename__ = 'room'

    AutoID = db.Column(db.BigInteger, primary_key=True, info='自增的主键')
    RoomID = db.Column(db.BigInteger, info='房间id')
    HotelID = db.Column(db.BigInteger, info='酒店id')
    RoomNum = db.Column(db.String(20), info='房间号')
    RoomTypeID = db.Column(db.BigInteger, info='房间种类id')
    RoomStatus = db.Column(db.Integer, server_default=db.FetchedValue(), info='0---空闲，1---占用')
    IsDeleted = db.Column(db.Integer, server_default=db.FetchedValue(), info='0--未删除，1--删除')
    CreateTime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='创建时间')
