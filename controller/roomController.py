#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.roomModel import Room
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class RoomController(Room):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = Room(
                RoomID=kwargs.get('RoomID'),
                HotelID=kwargs.get('HotelID'),
                RoomNum=kwargs.get('RoomNum'),
                RoomTypeID=kwargs.get('RoomTypeID'),
                RoomStatus=kwargs.get('RoomStatus'),
                CreateTime=kwargs.get('CreateTime'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'RoomID': model.RoomID,
                
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
            if kwargs.get('RoomID'):
                filter_list.append(cls.RoomID == kwargs['RoomID'])
            else:
                if kwargs.get('HotelID') is not None:
                    filter_list.append(cls.HotelID == kwargs.get('HotelID'))
                if kwargs.get('RoomNum'):
                    filter_list.append(cls.RoomNum == kwargs.get('RoomNum'))
                if kwargs.get('RoomTypeID') is not None:
                    filter_list.append(cls.RoomTypeID == kwargs.get('RoomTypeID'))
                if kwargs.get('RoomStatus') is not None:
                    filter_list.append(cls.RoomStatus == kwargs.get('RoomStatus'))
                if kwargs.get('CreateTime'):
                    filter_list.append(cls.CreateTime == kwargs.get('CreateTime'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            room_info = db.session.query(cls).filter(*filter_list)
            
            count = room_info.count()
            pages = math.ceil(count / size)
            room_info = room_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(room_info)
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
            if kwargs.get('RoomID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('RoomID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.RoomID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('HotelID') is not None:
                    filter_list.append(cls.HotelID == kwargs.get('HotelID'))
                if kwargs.get('RoomNum'):
                    filter_list.append(cls.RoomNum == kwargs.get('RoomNum'))
                if kwargs.get('RoomTypeID') is not None:
                    filter_list.append(cls.RoomTypeID == kwargs.get('RoomTypeID'))
                if kwargs.get('RoomStatus') is not None:
                    filter_list.append(cls.RoomStatus == kwargs.get('RoomStatus'))
                if kwargs.get('CreateTime'):
                    filter_list.append(cls.CreateTime == kwargs.get('CreateTime'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'RoomID': []
            }
            for query_model in res.all():
                results['RoomID'].append(query_model.RoomID)

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
            
            filter_list = [cls.IsDeleted == 0]
            filter_list.append(cls.RoomID == kwargs.get('RoomID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'RoomID': res.first().RoomID,
                
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
        param_list = json.loads(kwargs.get('RoomList'))
        model_list = []
        for param_dict in param_list:
            
            model = Room(
                RoomID=param_dict.get('RoomID'),
                HotelID=param_dict.get('HotelID'),
                RoomNum=param_dict.get('RoomNum'),
                RoomTypeID=param_dict.get('RoomTypeID'),
                RoomStatus=param_dict.get('RoomStatus'),
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
                added_record['RoomID'] = model.RoomID
                
                results['added_records'].append(added_record)
            
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
