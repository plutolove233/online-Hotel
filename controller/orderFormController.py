#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.orderFormModel import OrderForm
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class OrderFormController(OrderForm):

    # add
    @classmethod
    def add(cls, **kwargs):
        
        try:
            model = OrderForm(
                OrderFormID=kwargs.get('OrderFormID'),
                UserID=kwargs.get('UserID'),
                GuestID=kwargs.get('GuestID'),
                GuestName=kwargs.get('GuestName'),
                GuestPhone=kwargs.get('GuestPhone'),
                RoomID=kwargs.get('RoomID'),
                ArrivalTime=kwargs.get('ArrivalTime'),
                CheckOutTime=kwargs.get('CheckOutTime'),
                OrderFormStatus=kwargs.get('OrderFormStatus'),
                CreateTime=kwargs.get('CreateTime'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'OrderFormID': model.OrderFormID,
                
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
            if kwargs.get('OrderFormID'):
                filter_list.append(cls.OrderFormID == kwargs['OrderFormID'])
            else:
                if kwargs.get('UserID') is not None:
                    filter_list.append(cls.UserID == kwargs.get('UserID'))
                if kwargs.get('GuestID'):
                    filter_list.append(cls.GuestID == kwargs.get('GuestID'))
                if kwargs.get('GuestName'):
                    filter_list.append(cls.GuestName == kwargs.get('GuestName'))
                if kwargs.get('GuestPhone'):
                    filter_list.append(cls.GuestPhone == kwargs.get('GuestPhone'))
                if kwargs.get('RoomID') is not None:
                    filter_list.append(cls.RoomID == kwargs.get('RoomID'))
                if kwargs.get('ArrivalTime'):
                    filter_list.append(cls.ArrivalTime == kwargs.get('ArrivalTime'))
                if kwargs.get('CheckOutTime'):
                    filter_list.append(cls.CheckOutTime == kwargs.get('CheckOutTime'))
                if kwargs.get('OrderFormStatus') is not None:
                    filter_list.append(cls.OrderFormStatus == kwargs.get('OrderFormStatus'))
                if kwargs.get('CreateTime'):
                    filter_list.append(cls.CreateTime == kwargs.get('CreateTime'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            order_form_info = db.session.query(cls).filter(*filter_list)
            
            count = order_form_info.count()
            pages = math.ceil(count / size)
            order_form_info = order_form_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(order_form_info)
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
            if kwargs.get('OrderFormID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('OrderFormID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.OrderFormID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('UserID') is not None:
                    filter_list.append(cls.UserID == kwargs.get('UserID'))
                if kwargs.get('GuestID'):
                    filter_list.append(cls.GuestID == kwargs.get('GuestID'))
                if kwargs.get('GuestName'):
                    filter_list.append(cls.GuestName == kwargs.get('GuestName'))
                if kwargs.get('GuestPhone'):
                    filter_list.append(cls.GuestPhone == kwargs.get('GuestPhone'))
                if kwargs.get('RoomID') is not None:
                    filter_list.append(cls.RoomID == kwargs.get('RoomID'))
                if kwargs.get('ArrivalTime'):
                    filter_list.append(cls.ArrivalTime == kwargs.get('ArrivalTime'))
                if kwargs.get('CheckOutTime'):
                    filter_list.append(cls.CheckOutTime == kwargs.get('CheckOutTime'))
                if kwargs.get('OrderFormStatus') is not None:
                    filter_list.append(cls.OrderFormStatus == kwargs.get('OrderFormStatus'))
                if kwargs.get('CreateTime'):
                    filter_list.append(cls.CreateTime == kwargs.get('CreateTime'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'OrderFormID': []
            }
            for query_model in res.all():
                results['OrderFormID'].append(query_model.OrderFormID)

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
            filter_list.append(cls.OrderFormID == kwargs.get('OrderFormID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'OrderFormID': res.first().OrderFormID,
                
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
        param_list = json.loads(kwargs.get('OrderFormList'))
        model_list = []
        for param_dict in param_list:
            
            model = OrderForm(
                OrderFormID=param_dict.get('OrderFormID'),
                UserID=param_dict.get('UserID'),
                GuestID=param_dict.get('GuestID'),
                GuestName=param_dict.get('GuestName'),
                GuestPhone=param_dict.get('GuestPhone'),
                RoomID=param_dict.get('RoomID'),
                ArrivalTime=param_dict.get('ArrivalTime'),
                CheckOutTime=param_dict.get('CheckOutTime'),
                OrderFormStatus=param_dict.get('OrderFormStatus'),
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
                added_record['OrderFormID'] = model.OrderFormID
                
                results['added_records'].append(added_record)
            
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
