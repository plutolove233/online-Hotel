#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.remarkModel import Remark
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class RemarkController(Remark):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = Remark(
                RemarkID=kwargs.get('RemarkID'),
                RemarkContent=kwargs.get('RemarkContent'),
                HotelID=kwargs.get('HotelID'),
                RemarkUserID=kwargs.get('RemarkUserID'),
                CreateTime=kwargs.get('CreateTime'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'RemarkID': model.RemarkID,
                
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
            if kwargs.get('RemarkID'):
                filter_list.append(cls.RemarkID == kwargs['RemarkID'])
            else:
                if kwargs.get('RemarkContent'):
                    filter_list.append(cls.RemarkContent == kwargs.get('RemarkContent'))
                if kwargs.get('HotelID') is not None:
                    filter_list.append(cls.HotelID == kwargs.get('HotelID'))
                if kwargs.get('RemarkUserID') is not None:
                    filter_list.append(cls.RemarkUserID == kwargs.get('RemarkUserID'))
                if kwargs.get('CreateTime'):
                    filter_list.append(cls.CreateTime == kwargs.get('CreateTime'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            remark_info = db.session.query(cls).filter(*filter_list)
            
            count = remark_info.count()
            pages = math.ceil(count / size)
            remark_info = remark_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(remark_info)
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
            if kwargs.get('RemarkID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('RemarkID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.RemarkID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('RemarkContent'):
                    filter_list.append(cls.RemarkContent == kwargs.get('RemarkContent'))
                if kwargs.get('HotelID') is not None:
                    filter_list.append(cls.HotelID == kwargs.get('HotelID'))
                if kwargs.get('RemarkUserID') is not None:
                    filter_list.append(cls.RemarkUserID == kwargs.get('RemarkUserID'))
                if kwargs.get('CreateTime'):
                    filter_list.append(cls.CreateTime == kwargs.get('CreateTime'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'RemarkID': []
            }
            for query_model in res.all():
                results['RemarkID'].append(query_model.RemarkID)

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
            filter_list.append(cls.RemarkID == kwargs.get('RemarkID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'RemarkID': res.first().RemarkID,
                
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
        param_list = json.loads(kwargs.get('RemarkList'))
        model_list = []
        for param_dict in param_list:
            
            model = Remark(
                RemarkID=param_dict.get('RemarkID'),
                RemarkContent=param_dict.get('RemarkContent'),
                HotelID=param_dict.get('HotelID'),
                RemarkUserID=param_dict.get('RemarkUserID'),
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
                added_record['RemarkID'] = model.RemarkID
                
                results['added_records'].append(added_record)
            
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
