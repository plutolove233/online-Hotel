#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.hotelController import HotelController
from utils import commons
from utils.response_code import RET


class HotelResource(Resource):

    # get
    @classmethod
    def get(cls, HotelID=None):
        if HotelID:
            kwargs = {
                'HotelID': HotelID
            }

            res = HotelController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('HotelName', location='args', required=False, help='HotelName参数类型不正确或缺失')
        parser.add_argument('HotelAccount', location='args', required=False, help='HotelAccount参数类型不正确或缺失')
        parser.add_argument('Phone', location='args', required=False, help='Phone参数类型不正确或缺失')
        parser.add_argument('Email', location='args', required=False, help='Email参数类型不正确或缺失')
        parser.add_argument('Province', location='args', required=False, help='Province参数类型不正确或缺失')
        parser.add_argument('City', location='args', required=False, help='City参数类型不正确或缺失')
        parser.add_argument('Area', location='args', required=False, help='Area参数类型不正确或缺失')
        parser.add_argument('HotelPicUrl', location='args', required=False, help='HotelPicUrl参数类型不正确或缺失')
        parser.add_argument('HotelLabels', location='args', required=False, help='HotelLabels参数类型不正确或缺失')
        parser.add_argument('HotelDist', location='args', required=False, help='HotelDist参数类型不正确或缺失')
        parser.add_argument('CreateTime', location='args', required=False, help='CreateTime参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = HotelController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, HotelID=None):
        if HotelID:
            kwargs = {
                'HotelID': HotelID
            }

        else:
            parser = reqparse.RequestParser()
            parser.add_argument('HotelName', location='form', required=False, help='HotelName参数类型不正确或缺失')
            parser.add_argument('HotelAccount', location='form', required=False, help='HotelAccount参数类型不正确或缺失')
            parser.add_argument('Password', location='form', required=False, help='Password参数类型不正确或缺失')
            parser.add_argument('Phone', location='form', required=False, help='Phone参数类型不正确或缺失')
            parser.add_argument('Email', location='form', required=False, help='Email参数类型不正确或缺失')
            parser.add_argument('Province', location='form', required=False, help='Province参数类型不正确或缺失')
            parser.add_argument('City', location='form', required=False, help='City参数类型不正确或缺失')
            parser.add_argument('Area', location='form', required=False, help='Area参数类型不正确或缺失')
            parser.add_argument('HotelPicUrl', location='form', required=False, help='HotelPicUrl参数类型不正确或缺失')
            parser.add_argument('HotelLabels', location='form', required=False, help='HotelLabels参数类型不正确或缺失')
            parser.add_argument('HotelDist', location='form', required=False, help='HotelDist参数类型不正确或缺失')
            parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
            
            # Pass in the ID list for multiple deletions
            parser.add_argument('HotelID', type=str, location='form', required=False, help='HotelID参数类型不正确或缺失')

            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

        res = HotelController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, HotelID):
        if not HotelID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('HotelName', location='form', required=False, help='HotelName参数类型不正确或缺失')
        parser.add_argument('HotelAccount', location='form', required=False, help='HotelAccount参数类型不正确或缺失')
        parser.add_argument('Password', location='form', required=False, help='Password参数类型不正确或缺失')
        parser.add_argument('Phone', location='form', required=False, help='Phone参数类型不正确或缺失')
        parser.add_argument('Email', location='form', required=False, help='Email参数类型不正确或缺失')
        parser.add_argument('Province', location='form', required=False, help='Province参数类型不正确或缺失')
        parser.add_argument('City', location='form', required=False, help='City参数类型不正确或缺失')
        parser.add_argument('Area', location='form', required=False, help='Area参数类型不正确或缺失')
        parser.add_argument('HotelPicUrl', location='form', required=False, help='HotelPicUrl参数类型不正确或缺失')
        parser.add_argument('HotelLabels', location='form', required=False, help='HotelLabels参数类型不正确或缺失')
        parser.add_argument('HotelDist', location='form', required=False, help='HotelDist参数类型不正确或缺失')
        parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['HotelID'] = HotelID

        res = HotelController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        HotelList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('HotelList', type=str, location='form', required=False, help='HotelList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('HotelList'):
            res = HotelController.add_list(**kwargs)

        else:
            parser.add_argument('HotelID', location='form', required=False, help='HotelID参数类型不正确或缺失')
            parser.add_argument('HotelName', location='form', required=False, help='HotelName参数类型不正确或缺失')
            parser.add_argument('HotelAccount', location='form', required=False, help='HotelAccount参数类型不正确或缺失')
            parser.add_argument('Password', location='form', required=True, help='Password参数类型不正确或缺失')
            parser.add_argument('Phone', location='form', required=False, help='Phone参数类型不正确或缺失')
            parser.add_argument('Email', location='form', required=False, help='Email参数类型不正确或缺失')
            parser.add_argument('Province', location='form', required=False, help='Province参数类型不正确或缺失')
            parser.add_argument('City', location='form', required=False, help='City参数类型不正确或缺失')
            parser.add_argument('Area', location='form', required=False, help='Area参数类型不正确或缺失')
            parser.add_argument('HotelPicUrl', location='form', required=False, help='HotelPicUrl参数类型不正确或缺失')
            parser.add_argument('HotelLabels', location='form', required=False, help='HotelLabels参数类型不正确或缺失')
            parser.add_argument('HotelDist', location='form', required=False, help='HotelDist参数类型不正确或缺失')
            parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = HotelController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
