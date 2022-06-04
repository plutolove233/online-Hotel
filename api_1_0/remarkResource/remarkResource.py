#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.remarkController import RemarkController
from utils import commons
from utils.response_code import RET


class RemarkResource(Resource):

    # get
    @classmethod
    def get(cls, RemarkID=None):
        if RemarkID:
            kwargs = {
                'RemarkID': RemarkID
            }

            res = RemarkController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('RemarkContent', location='args', required=False, help='RemarkContent参数类型不正确或缺失')
        parser.add_argument('RemarkUserID', location='args', required=False, help='RemarkUserID参数类型不正确或缺失')
        parser.add_argument('CreateTime', location='args', required=False, help='CreateTime参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = RemarkController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, RemarkID=None):
        if RemarkID:
            kwargs = {
                'RemarkID': RemarkID
            }

        else:
            parser = reqparse.RequestParser()
            parser.add_argument('RemarkContent', location='form', required=False, help='RemarkContent参数类型不正确或缺失')
            parser.add_argument('RemarkUserID', location='form', required=False, help='RemarkUserID参数类型不正确或缺失')
            parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
            
            # Pass in the ID list for multiple deletions
            parser.add_argument('RemarkID', type=str, location='form', required=False, help='RemarkID参数类型不正确或缺失')

            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

        res = RemarkController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, RemarkID):
        if not RemarkID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('RemarkContent', location='form', required=False, help='RemarkContent参数类型不正确或缺失')
        parser.add_argument('RemarkUserID', location='form', required=False, help='RemarkUserID参数类型不正确或缺失')
        parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['RemarkID'] = RemarkID

        res = RemarkController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        RemarkList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('RemarkList', type=str, location='form', required=False, help='RemarkList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('RemarkList'):
            res = RemarkController.add_list(**kwargs)

        else:
            parser.add_argument('RemarkID', location='form', required=False, help='RemarkID参数类型不正确或缺失')
            parser.add_argument('RemarkContent', location='form', required=False, help='RemarkContent参数类型不正确或缺失')
            parser.add_argument('RemarkUserID', location='form', required=False, help='RemarkUserID参数类型不正确或缺失')
            parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = RemarkController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
