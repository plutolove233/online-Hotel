#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.roomController import RoomController
from utils import commons
from utils.response_code import RET


class RoomResource(Resource):

    # get
    @classmethod
    def get(cls, RoomID=None):
        if RoomID:
            kwargs = {
                'RoomID': RoomID
            }

            res = RoomController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('HotelID', location='args', required=False, help='HotelID参数类型不正确或缺失')
        parser.add_argument('RoomNum', location='args', required=False, help='RoomNum参数类型不正确或缺失')
        parser.add_argument('RoomTypeID', location='args', required=False, help='RoomTypeID参数类型不正确或缺失')
        parser.add_argument('RoomBrief', location='args', required=False, help='RoomBrief参数类型不正确或缺失')
        parser.add_argument('RoomStatus', location='args', required=False, help='RoomStatus参数类型不正确或缺失')
        parser.add_argument('CreateTime', location='args', required=False, help='CreateTime参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = RoomController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, RoomID=None):
        if RoomID:
            kwargs = {
                'RoomID': RoomID
            }

        else:
            parser = reqparse.RequestParser()
            parser.add_argument('HotelID', location='form', required=False, help='HotelID参数类型不正确或缺失')
            parser.add_argument('RoomNum', location='form', required=False, help='RoomNum参数类型不正确或缺失')
            parser.add_argument('RoomTypeID', location='form', required=False, help='RoomTypeID参数类型不正确或缺失')
            parser.add_argument('RoomBrief', location='form', required=False, help='RoomBrief参数类型不正确或缺失')
            parser.add_argument('RoomStatus', location='form', required=False, help='RoomStatus参数类型不正确或缺失')
            parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
            
            # Pass in the ID list for multiple deletions
            parser.add_argument('RoomID', type=str, location='form', required=False, help='RoomID参数类型不正确或缺失')

            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

        res = RoomController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, RoomID):
        if not RoomID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('HotelID', location='form', required=False, help='HotelID参数类型不正确或缺失')
        parser.add_argument('RoomNum', location='form', required=False, help='RoomNum参数类型不正确或缺失')
        parser.add_argument('RoomTypeID', location='form', required=False, help='RoomTypeID参数类型不正确或缺失')
        parser.add_argument('RoomBrief', location='form', required=False, help='RoomBrief参数类型不正确或缺失')
        parser.add_argument('RoomStatus', location='form', required=False, help='RoomStatus参数类型不正确或缺失')
        parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['RoomID'] = RoomID

        res = RoomController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        RoomList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('RoomList', type=str, location='form', required=False, help='RoomList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('RoomList'):
            res = RoomController.add_list(**kwargs)

        else:
            parser.add_argument('RoomID', location='form', required=False, help='RoomID参数类型不正确或缺失')
            parser.add_argument('HotelID', location='form', required=False, help='HotelID参数类型不正确或缺失')
            parser.add_argument('RoomNum', location='form', required=False, help='RoomNum参数类型不正确或缺失')
            parser.add_argument('RoomTypeID', location='form', required=False, help='RoomTypeID参数类型不正确或缺失')
            parser.add_argument('RoomBrief', location='form', required=False, help='RoomBrief参数类型不正确或缺失')
            parser.add_argument('RoomStatus', location='form', required=False, help='RoomStatus参数类型不正确或缺失')
            parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = RoomController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
