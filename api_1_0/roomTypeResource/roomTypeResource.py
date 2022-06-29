#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.roomTypeController import RoomTypeController
from utils import commons
from utils.response_code import RET


class RoomTypeResource(Resource):

    # get
    @classmethod
    def get(cls, RoomTypeID=None):
        if RoomTypeID:
            kwargs = {
                'RoomTypeID': RoomTypeID
            }

            res = RoomTypeController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('HotelID', location='args', required=False, help='HotelID参数类型不正确或缺失')
        parser.add_argument('RoomTypeName', location='args', required=False, help='RoomTypeName参数类型不正确或缺失')
        parser.add_argument('Square', location='args', required=False, help='Square参数类型不正确或缺失')
        parser.add_argument('Floor', location='args', required=False, help='Floor参数类型不正确或缺失')
        parser.add_argument('WindowDescription', location='args', required=False, help='WindowDescription参数类型不正确或缺失')
        parser.add_argument('Price', location='args', required=False, help='Price参数类型不正确或缺失')
        parser.add_argument('RoomTypeBrief', location='args', required=False, help='RoomTypeBrief参数类型不正确或缺失')
        parser.add_argument('RoomPicUrl', location='args', required=False, help='RoomPicUrl参数类型不正确或缺失')
        parser.add_argument('CreateTime', location='args', required=False, help='CreateTime参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = RoomTypeController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, RoomTypeID=None):
        if RoomTypeID:
            kwargs = {
                'RoomTypeID': RoomTypeID
            }

        else:
            parser = reqparse.RequestParser()
            parser.add_argument('HotelID', location='form', required=False, help='HotelID参数类型不正确或缺失')
            parser.add_argument('RoomTypeName', location='form', required=False, help='RoomTypeName参数类型不正确或缺失')
            parser.add_argument('Square', location='form', required=False, help='Square参数类型不正确或缺失')
            parser.add_argument('Floor', location='form', required=False, help='Floor参数类型不正确或缺失')
            parser.add_argument('WindowDescription', location='form', required=False, help='WindowDescription参数类型不正确或缺失')
            parser.add_argument('Price', location='form', required=False, help='Price参数类型不正确或缺失')
            parser.add_argument('RoomTypeBrief', location='form', required=False, help='RoomTypeBrief参数类型不正确或缺失')
            parser.add_argument('RoomPicUrl', location='form', required=False, help='RoomPicUrl参数类型不正确或缺失')
            parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
            
            # Pass in the ID list for multiple deletions
            parser.add_argument('RoomTypeID', type=str, location='form', required=False, help='RoomTypeID参数类型不正确或缺失')

            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

        res = RoomTypeController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, RoomTypeID):
        if not RoomTypeID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('HotelID', location='form', required=False, help='HotelID参数类型不正确或缺失')
        parser.add_argument('RoomTypeName', location='form', required=False, help='RoomTypeName参数类型不正确或缺失')
        parser.add_argument('Square', location='form', required=False, help='Square参数类型不正确或缺失')
        parser.add_argument('Floor', location='form', required=False, help='Floor参数类型不正确或缺失')
        parser.add_argument('WindowDescription', location='form', required=False, help='WindowDescription参数类型不正确或缺失')
        parser.add_argument('Price', location='form', required=False, help='Price参数类型不正确或缺失')
        parser.add_argument('RoomTypeBrief', location='form', required=False, help='RoomTypeBrief参数类型不正确或缺失')
        parser.add_argument('RoomPicUrl', location='form', required=False, help='RoomPicUrl参数类型不正确或缺失')
        parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['RoomTypeID'] = RoomTypeID

        res = RoomTypeController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        RoomTypeList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('RoomTypeList', type=str, location='form', required=False, help='RoomTypeList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('RoomTypeList'):
            res = RoomTypeController.add_list(**kwargs)

        else:
            parser.add_argument('RoomTypeID', location='form', required=False, help='RoomTypeID参数类型不正确或缺失')
            parser.add_argument('HotelID', location='form', required=False, help='HotelID参数类型不正确或缺失')
            parser.add_argument('RoomTypeName', location='form', required=False, help='RoomTypeName参数类型不正确或缺失')
            parser.add_argument('Square', location='form', required=False, help='Square参数类型不正确或缺失')
            parser.add_argument('Floor', location='form', required=False, help='Floor参数类型不正确或缺失')
            parser.add_argument('WindowDescription', location='form', required=False, help='WindowDescription参数类型不正确或缺失')
            parser.add_argument('Price', location='form', required=False, help='Price参数类型不正确或缺失')
            parser.add_argument('RoomTypeBrief', location='form', required=False, help='RoomTypeBrief参数类型不正确或缺失')
            parser.add_argument('RoomPicUrl', location='form', required=False, help='RoomPicUrl参数类型不正确或缺失')
            parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = RoomTypeController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
