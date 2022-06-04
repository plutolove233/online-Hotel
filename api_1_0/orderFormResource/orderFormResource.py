#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.orderFormController import OrderFormController
from utils import commons
from utils.response_code import RET


class OrderFormResource(Resource):

    # get
    @classmethod
    def get(cls, OrderFormID=None):
        if OrderFormID:
            kwargs = {
                'OrderFormID': OrderFormID
            }

            res = OrderFormController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('UserID', location='args', required=False, help='UserID参数类型不正确或缺失')
        parser.add_argument('GuestID', location='args', required=False, help='GuestID参数类型不正确或缺失')
        parser.add_argument('GuestName', location='args', required=False, help='GuestName参数类型不正确或缺失')
        parser.add_argument('GuestPhone', location='args', required=False, help='GuestPhone参数类型不正确或缺失')
        parser.add_argument('RoomID', location='args', required=False, help='RoomID参数类型不正确或缺失')
        parser.add_argument('ArrivalTime', location='args', required=False, help='ArrivalTime参数类型不正确或缺失')
        parser.add_argument('CheckOutTime', location='args', required=False, help='CheckOutTime参数类型不正确或缺失')
        parser.add_argument('OrderFormStatus', location='args', required=False, help='OrderFormStatus参数类型不正确或缺失')
        parser.add_argument('CreateTime', location='args', required=False, help='CreateTime参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = OrderFormController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, OrderFormID=None):
        if OrderFormID:
            kwargs = {
                'OrderFormID': OrderFormID
            }

        else:
            parser = reqparse.RequestParser()
            parser.add_argument('UserID', location='form', required=False, help='UserID参数类型不正确或缺失')
            parser.add_argument('GuestID', location='form', required=False, help='GuestID参数类型不正确或缺失')
            parser.add_argument('GuestName', location='form', required=False, help='GuestName参数类型不正确或缺失')
            parser.add_argument('GuestPhone', location='form', required=False, help='GuestPhone参数类型不正确或缺失')
            parser.add_argument('RoomID', location='form', required=False, help='RoomID参数类型不正确或缺失')
            parser.add_argument('ArrivalTime', location='form', required=False, help='ArrivalTime参数类型不正确或缺失')
            parser.add_argument('CheckOutTime', location='form', required=False, help='CheckOutTime参数类型不正确或缺失')
            parser.add_argument('OrderFormStatus', location='form', required=False, help='OrderFormStatus参数类型不正确或缺失')
            parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
            
            # Pass in the ID list for multiple deletions
            parser.add_argument('OrderFormID', type=str, location='form', required=False, help='OrderFormID参数类型不正确或缺失')

            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

        res = OrderFormController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, OrderFormID):
        if not OrderFormID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('UserID', location='form', required=False, help='UserID参数类型不正确或缺失')
        parser.add_argument('GuestID', location='form', required=False, help='GuestID参数类型不正确或缺失')
        parser.add_argument('GuestName', location='form', required=False, help='GuestName参数类型不正确或缺失')
        parser.add_argument('GuestPhone', location='form', required=False, help='GuestPhone参数类型不正确或缺失')
        parser.add_argument('RoomID', location='form', required=False, help='RoomID参数类型不正确或缺失')
        parser.add_argument('ArrivalTime', location='form', required=False, help='ArrivalTime参数类型不正确或缺失')
        parser.add_argument('CheckOutTime', location='form', required=False, help='CheckOutTime参数类型不正确或缺失')
        parser.add_argument('OrderFormStatus', location='form', required=False, help='OrderFormStatus参数类型不正确或缺失')
        parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['OrderFormID'] = OrderFormID

        res = OrderFormController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        OrderFormList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('OrderFormList', type=str, location='form', required=False, help='OrderFormList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('OrderFormList'):
            res = OrderFormController.add_list(**kwargs)

        else:
            parser.add_argument('OrderFormID', location='form', required=False, help='OrderFormID参数类型不正确或缺失')
            parser.add_argument('UserID', location='form', required=False, help='UserID参数类型不正确或缺失')
            parser.add_argument('GuestID', location='form', required=False, help='GuestID参数类型不正确或缺失')
            parser.add_argument('GuestName', location='form', required=False, help='GuestName参数类型不正确或缺失')
            parser.add_argument('GuestPhone', location='form', required=False, help='GuestPhone参数类型不正确或缺失')
            parser.add_argument('RoomID', location='form', required=False, help='RoomID参数类型不正确或缺失')
            parser.add_argument('ArrivalTime', location='form', required=False, help='ArrivalTime参数类型不正确或缺失')
            parser.add_argument('CheckOutTime', location='form', required=False, help='CheckOutTime参数类型不正确或缺失')
            parser.add_argument('OrderFormStatus', location='form', required=False, help='OrderFormStatus参数类型不正确或缺失')
            parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = OrderFormController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
