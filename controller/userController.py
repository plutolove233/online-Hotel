#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.userModel import User
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings
from utils.rsa_encryption_decryption import RSAEncryptionDecryption


class UserController(User):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = User(
                UserID=kwargs.get('UserID'),
                UserName=kwargs.get('UserName'),
                Password=RSAEncryptionDecryption.encrypt(kwargs.get('Password')) if kwargs.get('Password') else None,
                Phone=kwargs.get('Phone'),
                Email=kwargs.get('Email'),
                IsInRoom=kwargs.get('IsInRoom'),
                FaceUrl=kwargs.get('FaceUrl'),
                CreateTime=kwargs.get('CreateTime'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'UserID': model.UserID,
                
            }
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # get
    @classmethod
    def get(cls, **kwargs):
        try:
            filter_list = [cls.IsDeleted == 0]
            if kwargs.get('UserID'):
                filter_list.append(cls.UserID == kwargs['UserID'])
            else:
                if kwargs.get('UserName'):
                    filter_list.append(cls.UserName == kwargs.get('UserName'))
                if kwargs.get('Phone'):
                    filter_list.append(cls.Phone == kwargs.get('Phone'))
                if kwargs.get('Email'):
                    filter_list.append(cls.Email == kwargs.get('Email'))
                if kwargs.get('IsInRoom') is not None:
                    filter_list.append(cls.IsInRoom == kwargs.get('IsInRoom'))
                if kwargs.get('FaceUrl'):
                    filter_list.append(cls.FaceUrl == kwargs.get('FaceUrl'))
                if kwargs.get('CreateTime'):
                    filter_list.append(cls.CreateTime == kwargs.get('CreateTime'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            user_info = db.session.query(cls).filter(*filter_list)
            
            count = user_info.count()
            pages = math.ceil(count / size)
            user_info = user_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(user_info)
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'totalCount': count, 'totalPage': pages, 'data': results}
            
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # delete
    @classmethod
    def delete(cls, **kwargs):
        try:
            filter_list = [cls.IsDeleted == 0]
            if kwargs.get('UserID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('UserID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.UserID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('UserName'):
                    filter_list.append(cls.UserName == kwargs.get('UserName'))
                if kwargs.get('Phone'):
                    filter_list.append(cls.Phone == kwargs.get('Phone'))
                if kwargs.get('Email'):
                    filter_list.append(cls.Email == kwargs.get('Email'))
                if kwargs.get('IsInRoom') is not None:
                    filter_list.append(cls.IsInRoom == kwargs.get('IsInRoom'))
                if kwargs.get('FaceUrl'):
                    filter_list.append(cls.FaceUrl == kwargs.get('FaceUrl'))
                if kwargs.get('CreateTime'):
                    filter_list.append(cls.CreateTime == kwargs.get('CreateTime'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'UserID': []
            }
            for query_model in res.all():
                results['UserID'].append(query_model.UserID)

            res.update({'IsDeleted': 1})
            db.session.commit()

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}

        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
    
    # update
    @classmethod
    def update(cls, **kwargs):
        try:
            if kwargs.get('Password'):
                kwargs['Password'] = RSAEncryptionDecryption.encrypt(kwargs['Password'])
            
            filter_list = [cls.IsDeleted == 0]
            filter_list.append(cls.UserID == kwargs.get('UserID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'UserID': res.first().UserID,
                
            }
            
            res.update(kwargs)
            db.session.commit()

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}

        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # batch add
    @classmethod
    def add_list(cls, **kwargs):
        param_list = json.loads(kwargs.get('UserList'))
        model_list = []
        for param_dict in param_list:
            
            model = User(
                UserID=param_dict.get('UserID'),
                UserName=param_dict.get('UserName'),
                Password=RSAEncryptionDecryption.encrypt(param_dict.get('Password')),
                Phone=param_dict.get('Phone'),
                Email=param_dict.get('Email'),
                IsInRoom=param_dict.get('IsInRoom'),
                FaceUrl=param_dict.get('FaceUrl'),
                CreateTime=param_dict.get('CreateTime'),
                
            )
            model_list.append(model)
        
        try:
            db.session.add_all(model_list)
            db.session.commit()
            results = {
                'added_records': [],
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            for model in model_list:
                added_record = {}
                added_record['UserID'] = model.UserID
                
                results['added_records'].append(added_record)
            
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
