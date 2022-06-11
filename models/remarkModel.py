# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Remark(db.Model):
    __tablename__ = 'remark'

    AutoID = db.Column(db.BigInteger, primary_key=True, info='自增的主键')
    RemarkID = db.Column(db.BigInteger, info='评论id')
    RemarkContent = db.Column(db.String(600), info='评论内容')
    HotelID = db.Column(db.BigInteger, info='评论酒店id')
    RemarkUserID = db.Column(db.BigInteger, info='评论用户id')
    IsDeleted = db.Column(db.Integer, server_default=db.FetchedValue(), info='0--未删除，1--删除')
    CreateTime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='创建时间')
