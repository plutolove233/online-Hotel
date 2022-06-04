# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Hotel(db.Model):
    __tablename__ = 'hotel'

    AutoID = db.Column(db.BigInteger, primary_key=True, info='自增主键')
    HotelID = db.Column(db.BigInteger, info='酒店id')
    HotelName = db.Column(db.String(255), info='酒店名称')
    HotelAccount = db.Column(db.String(20), info='酒店账号昵称')
    Password = db.Column(db.String(255), info='酒店登录密码')
    Phone = db.Column(db.String(20), info='酒店联系电话')
    Email = db.Column(db.String(255), info='酒店邮箱')
    Province = db.Column(db.String(255), info='酒店所在省')
    City = db.Column(db.String(255), info='酒店所在市')
    Area = db.Column(db.String(255), info='酒店所在区')
    HotelPicUrl = db.Column(db.String(255), info='酒店图片地址')
    HotelLabels = db.Column(db.String(255), info="酒店标签，用'/‘隔开")
    HotelDist = db.Column(db.Float, info='酒店离市中心距离')
    IsDeleted = db.Column(db.Integer, server_default=db.FetchedValue(), info='0--未删除，1--删除')
    CreateTime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='创建时间')
