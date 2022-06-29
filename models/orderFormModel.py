# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class OrderForm(db.Model):
    __tablename__ = 'order_form'

    AutoID = db.Column(db.BigInteger, primary_key=True, info='自增的主键')
    OrderFormID = db.Column(db.BigInteger, info='订单id')
    UserID = db.Column(db.BigInteger, info='订单用户id')
    GuestID = db.Column(db.String(30), info='住客身份证')
    GuestName = db.Column(db.String(30), info='住客姓名')
    GuestPhone = db.Column(db.String(20), info='住客电话')
    HotelID = db.Column(db.BigInteger, info='订单所属酒店id')
    RoomID = db.Column(db.BigInteger, info='房间信息')
    ArrivalTime = db.Column(db.DateTime, info='到店时间')
    CheckOutTime = db.Column(db.DateTime, info='离店时间')
    OrderFormStatus = db.Column(db.Integer, server_default=db.FetchedValue(), info='0--未入住  1--入住')
    IsDeleted = db.Column(db.Integer, server_default=db.FetchedValue(), info='0--未删除，1--删除')
    CreateTime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='创建时间')
