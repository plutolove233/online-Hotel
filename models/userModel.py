# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'user'

    AutoID = db.Column(db.BigInteger, primary_key=True, info='自增的主键')
    UserID = db.Column(db.BigInteger, info='用户id')
    UserName = db.Column(db.String(255), info='用户名称')
    Password = db.Column(db.String(255), info='用户密码')
    Phone = db.Column(db.String(20), info='用户电话')
    Email = db.Column(db.String(255), info='邮箱')
    IsInRoom = db.Column(db.Integer, server_default=db.FetchedValue(), info='0--未入住，1--入住')
    FaceUrl = db.Column(db.String(255), info='用户头像地址')
    IsDeleted = db.Column(db.Integer, server_default=db.FetchedValue(), info='0--未删除，1--删除')
    CreateTime = db.Column(db.DateTime, server_default=db.FetchedValue(), info='创建时间')
