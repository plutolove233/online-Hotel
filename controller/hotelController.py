#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.hotelModel import Hotel
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings
from utils.rsa_encryption_decryption import RSAEncryptionDecryption


class HotelController(Hotel):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = Hotel(
                HotelID=kwargs.get('HotelID'),
                HotelName=kwargs.get('HotelName'),
                HotelAccount=kwargs.get('HotelAccount'),
                Password=RSAEncryptionDecryption.encrypt(kwargs.get('Password')) if kwargs.get('Password') else None,
                Phone=kwargs.get('Phone'),
                Email=kwargs.get('Email'),
                Province=kwargs.get('Province'),
                City=kwargs.get('City'),
                Area=kwargs.get('Area'),
                HotelPicUrl=kwargs.get('HotelPicUrl'),
                HotelLabels=kwargs.get('HotelLabels'),
                HotelDist=kwargs.get('HotelDist'),
                CreateTime=kwargs.get('CreateTime'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'HotelID': model.HotelID,
                
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
            if kwargs.get('HotelID'):
                filter_list.append(cls.HotelID == kwargs['HotelID'])
            else:
                if kwargs.get('HotelName'):
                    filter_list.append(cls.HotelName == kwargs.get('HotelName'))
                if kwargs.get('HotelAccount'):
                    filter_list.append(cls.HotelAccount == kwargs.get('HotelAccount'))
                if kwargs.get('Phone'):
                    filter_list.append(cls.Phone == kwargs.get('Phone'))
                if kwargs.get('Email'):
                    filter_list.append(cls.Email == kwargs.get('Email'))
                if kwargs.get('Province'):
                    filter_list.append(cls.Province == kwargs.get('Province'))
                if kwargs.get('City'):
                    filter_list.append(cls.City == kwargs.get('City'))
                if kwargs.get('Area'):
                    filter_list.append(cls.Area == kwargs.get('Area'))
                if kwargs.get('HotelPicUrl'):
                    filter_list.append(cls.HotelPicUrl == kwargs.get('HotelPicUrl'))
                if kwargs.get('HotelLabels'):
                    filter_list.append(cls.HotelLabels == kwargs.get('HotelLabels'))
                if kwargs.get('HotelDist') is not None:
                    filter_list.append(cls.HotelDist == kwargs.get('HotelDist'))
                if kwargs.get('CreateTime'):
                    filter_list.append(cls.CreateTime == kwargs.get('CreateTime'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            hotel_info = db.session.query(cls).filter(*filter_list)
            
            count = hotel_info.count()
            pages = math.ceil(count / size)
            hotel_info = hotel_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(hotel_info)
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
            if kwargs.get('HotelID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('HotelID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.HotelID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('HotelName'):
                    filter_list.append(cls.HotelName == kwargs.get('HotelName'))
                if kwargs.get('HotelAccount'):
                    filter_list.append(cls.HotelAccount == kwargs.get('HotelAccount'))
                if kwargs.get('Phone'):
                    filter_list.append(cls.Phone == kwargs.get('Phone'))
                if kwargs.get('Email'):
                    filter_list.append(cls.Email == kwargs.get('Email'))
                if kwargs.get('Province'):
                    filter_list.append(cls.Province == kwargs.get('Province'))
                if kwargs.get('City'):
                    filter_list.append(cls.City == kwargs.get('City'))
                if kwargs.get('Area'):
                    filter_list.append(cls.Area == kwargs.get('Area'))
                if kwargs.get('HotelPicUrl'):
                    filter_list.append(cls.HotelPicUrl == kwargs.get('HotelPicUrl'))
                if kwargs.get('HotelLabels'):
                    filter_list.append(cls.HotelLabels == kwargs.get('HotelLabels'))
                if kwargs.get('HotelDist') is not None:
                    filter_list.append(cls.HotelDist == kwargs.get('HotelDist'))
                if kwargs.get('CreateTime'):
                    filter_list.append(cls.CreateTime == kwargs.get('CreateTime'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'HotelID': []
            }
            for query_model in res.all():
                results['HotelID'].append(query_model.HotelID)

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
            filter_list.append(cls.HotelID == kwargs.get('HotelID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'HotelID': res.first().HotelID,
                
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
        param_list = json.loads(kwargs.get('HotelList'))
        model_list = []
        for param_dict in param_list:
            
            model = Hotel(
                HotelID=param_dict.get('HotelID'),
                HotelName=param_dict.get('HotelName'),
                HotelAccount=param_dict.get('HotelAccount'),
                Password=RSAEncryptionDecryption.encrypt(param_dict.get('Password')),
                Phone=param_dict.get('Phone'),
                Email=param_dict.get('Email'),
                Province=param_dict.get('Province'),
                City=param_dict.get('City'),
                Area=param_dict.get('Area'),
                HotelPicUrl=param_dict.get('HotelPicUrl'),
                HotelLabels=param_dict.get('HotelLabels'),
                HotelDist=param_dict.get('HotelDist'),
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
                added_record['HotelID'] = model.HotelID
                
                results['added_records'].append(added_record)
            
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
