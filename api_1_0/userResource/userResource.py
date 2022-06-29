#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.userController import UserController
from utils import commons
from utils.response_code import RET


class UserResource(Resource):

    # get
    @classmethod
    def get(cls, UserID=None):
        if UserID:
            kwargs = {
                'UserID': UserID
            }

            res = UserController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('UserName', location='args', required=False, help='UserName参数类型不正确或缺失')
        parser.add_argument('Phone', location='args', required=False, help='Phone参数类型不正确或缺失')
        parser.add_argument('Email', location='args', required=False, help='Email参数类型不正确或缺失')
        parser.add_argument('IsInRoom', location='args', required=False, help='IsInRoom参数类型不正确或缺失')
        parser.add_argument('FaceUrl', location='args', required=False, help='FaceUrl参数类型不正确或缺失')
        parser.add_argument('CreateTime', location='args', required=False, help='CreateTime参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = UserController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, UserID=None):
        if UserID:
            kwargs = {
                'UserID': UserID
            }

        else:
            parser = reqparse.RequestParser()
            parser.add_argument('UserName', location='form', required=False, help='UserName参数类型不正确或缺失')
            parser.add_argument('Password', location='form', required=False, help='Password参数类型不正确或缺失')
            parser.add_argument('Phone', location='form', required=False, help='Phone参数类型不正确或缺失')
            parser.add_argument('Email', location='form', required=False, help='Email参数类型不正确或缺失')
            parser.add_argument('IsInRoom', location='form', required=False, help='IsInRoom参数类型不正确或缺失')
            parser.add_argument('FaceUrl', location='form', required=False, help='FaceUrl参数类型不正确或缺失')
            parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
            
            # Pass in the ID list for multiple deletions
            parser.add_argument('UserID', type=str, location='form', required=False, help='UserID参数类型不正确或缺失')

            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

        res = UserController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, UserID):
        if not UserID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('UserName', location='form', required=False, help='UserName参数类型不正确或缺失')
        parser.add_argument('Password', location='form', required=False, help='Password参数类型不正确或缺失')
        parser.add_argument('Phone', location='form', required=False, help='Phone参数类型不正确或缺失')
        parser.add_argument('Email', location='form', required=False, help='Email参数类型不正确或缺失')
        parser.add_argument('IsInRoom', location='form', required=False, help='IsInRoom参数类型不正确或缺失')
        parser.add_argument('FaceUrl', location='form', required=False, help='FaceUrl参数类型不正确或缺失')
        parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['UserID'] = UserID

        res = UserController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        UserList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('UserList', type=str, location='form', required=False, help='UserList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('UserList'):
            res = UserController.add_list(**kwargs)

        else:
            parser.add_argument('UserID', location='form', required=False, help='UserID参数类型不正确或缺失')
            parser.add_argument('UserName', location='form', required=False, help='UserName参数类型不正确或缺失')
            parser.add_argument('Password', location='form', required=True, help='Password参数类型不正确或缺失')
            parser.add_argument('Phone', location='form', required=False, help='Phone参数类型不正确或缺失')
            parser.add_argument('Email', location='form', required=False, help='Email参数类型不正确或缺失')
            parser.add_argument('IsInRoom', location='form', required=False, help='IsInRoom参数类型不正确或缺失')
            parser.add_argument('FaceUrl', location='form', required=False, help='FaceUrl参数类型不正确或缺失')
            parser.add_argument('CreateTime', location='form', required=False, help='CreateTime参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = UserController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
