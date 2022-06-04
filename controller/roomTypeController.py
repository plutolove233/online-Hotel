#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.roomTypeModel import RoomType
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class RoomTypeController(RoomType):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = RoomType(
                RoomTypeID=kwargs.get('RoomTypeID'),
                HotelID=kwargs.get('HotelID'),
                RoomTypeName=kwargs.get('RoomTypeName'),
                Square=kwargs.get('Square'),
                Floor=kwargs.get('Floor'),
                WindowDescription=kwargs.get('WindowDescription'),
                Price=kwargs.get('Price'),
                RoomTypeBrief=kwargs.get('RoomTypeBrief'),
                RoomPicUrl=kwargs.get('RoomPicUrl'),
                CreateTime=kwargs.get('CreateTime'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'RoomTypeID': model.RoomTypeID,
                
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
            if kwargs.get('RoomTypeID'):
                filter_list.append(cls.RoomTypeID == kwargs['RoomTypeID'])
            else:
                if kwargs.get('HotelID') is not None:
                    filter_list.append(cls.HotelID == kwargs.get('HotelID'))
                if kwargs.get('RoomTypeName'):
                    filter_list.append(cls.RoomTypeName == kwargs.get('RoomTypeName'))
                if kwargs.get('Square') is not None:
                    filter_list.append(cls.Square == kwargs.get('Square'))
                if kwargs.get('Floor') is not None:
                    filter_list.append(cls.Floor == kwargs.get('Floor'))
                if kwargs.get('WindowDescription'):
                    filter_list.append(cls.WindowDescription == kwargs.get('WindowDescription'))
                if kwargs.get('Price') is not None:
                    filter_list.append(cls.Price == kwargs.get('Price'))
                if kwargs.get('RoomTypeBrief'):
                    filter_list.append(cls.RoomTypeBrief == kwargs.get('RoomTypeBrief'))
                if kwargs.get('RoomPicUrl'):
                    filter_list.append(cls.RoomPicUrl == kwargs.get('RoomPicUrl'))
                if kwargs.get('CreateTime'):
                    filter_list.append(cls.CreateTime == kwargs.get('CreateTime'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            room_type_info = db.session.query(cls).filter(*filter_list)
            
            count = room_type_info.count()
            pages = math.ceil(count / size)
            room_type_info = room_type_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(room_type_info)
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
            if kwargs.get('RoomTypeID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('RoomTypeID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.RoomTypeID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('HotelID') is not None:
                    filter_list.append(cls.HotelID == kwargs.get('HotelID'))
                if kwargs.get('RoomTypeName'):
                    filter_list.append(cls.RoomTypeName == kwargs.get('RoomTypeName'))
                if kwargs.get('Square') is not None:
                    filter_list.append(cls.Square == kwargs.get('Square'))
                if kwargs.get('Floor') is not None:
                    filter_list.append(cls.Floor == kwargs.get('Floor'))
                if kwargs.get('WindowDescription'):
                    filter_list.append(cls.WindowDescription == kwargs.get('WindowDescription'))
                if kwargs.get('Price') is not None:
                    filter_list.append(cls.Price == kwargs.get('Price'))
                if kwargs.get('RoomTypeBrief'):
                    filter_list.append(cls.RoomTypeBrief == kwargs.get('RoomTypeBrief'))
                if kwargs.get('RoomPicUrl'):
                    filter_list.append(cls.RoomPicUrl == kwargs.get('RoomPicUrl'))
                if kwargs.get('CreateTime'):
                    filter_list.append(cls.CreateTime == kwargs.get('CreateTime'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'RoomTypeID': []
            }
            for query_model in res.all():
                results['RoomTypeID'].append(query_model.RoomTypeID)

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
            filter_list.append(cls.RoomTypeID == kwargs.get('RoomTypeID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'RoomTypeID': res.first().RoomTypeID,
                
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
        param_list = json.loads(kwargs.get('RoomTypeList'))
        model_list = []
        for param_dict in param_list:
            
            model = RoomType(
                RoomTypeID=param_dict.get('RoomTypeID'),
                HotelID=param_dict.get('HotelID'),
                RoomTypeName=param_dict.get('RoomTypeName'),
                Square=param_dict.get('Square'),
                Floor=param_dict.get('Floor'),
                WindowDescription=param_dict.get('WindowDescription'),
                Price=param_dict.get('Price'),
                RoomTypeBrief=param_dict.get('RoomTypeBrief'),
                RoomPicUrl=param_dict.get('RoomPicUrl'),
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
                added_record['RoomTypeID'] = model.RoomTypeID
                
                results['added_records'].append(added_record)
            
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
