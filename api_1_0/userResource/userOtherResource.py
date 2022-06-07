#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask_restful import reqparse,Resource
from flask import jsonify
from werkzeug.exceptions import BadRequest

from service.hotelService import HotelService
from utils import commons
from utils.commons import put_remove_none
from utils.generate_id import GenerateID
from service.userService import UserService
from utils.myLogging import logger
from utils.response_code import RET, error_map_EN


class UserRegisterResource(Resource):
	@classmethod
	def post(cls):
		parser = reqparse.RequestParser()
		parser.add_argument('UserName', location='form', required=True, type=str, help='UserName参数类型不正确或缺失')
		parser.add_argument('Password', location='form', required=True, type=str, help='Password参数类型不正确或缺失')
		parser.add_argument('Phone', location='form', required=False, type=str, help='Phone参数类型不正确或缺失')
		parser.add_argument('Email', location='form', required=False, type=str, help='Email参数类型不正确或缺失')
		try:
			kwargs = parser.parse_args()

			res = UserService.get(Phone=kwargs.get("Phone"))
			if res.get("code") != RET.OK:
				logger.error(error_map_EN(res.get("code")))
				return jsonify({
					"code":res.get("code"),
					"error":res.get("data").get("error"),
					"message":res.get("message"),
				})
			if res.get("totalCount") != 0:
				logger.error(error_map_EN(RET.DATAEXIST))
				return jsonify({
					"code":RET.DATAEXIST,
					"error":error_map_EN[RET.DATAEXIST],
					"message":"用户手机信息已注册",
				})

			kwargs['UserID'] = int(GenerateID.create_random_id())
			kwargs['FaceUrl'] = 'user/default.jpg'
			kwargs = commons.put_remove_none(**kwargs)
			res = UserService.add(**kwargs)
			if res.get("code") != RET.OK:
				logger.error(res.get("data").get("error"))
				return jsonify({
					"code":res.get("code"),
					"error":res.get("data").get("error"),
					"message":"用户注册失败",
				})
			logger.info(f"user {kwargs['UserID']} register success")
			return jsonify({
				"code": RET.OK,
				"message": "用户注册成功",
			})
		except BadRequest as e:
			logger.error(str(e))
			return jsonify({
				"code":RET.PARAMERR,
				"error":str(e),
				"message":"获取请求参数失败",
			})
		except Exception as e:
			logger.warning(str(e))
			return jsonify({
				"code":RET.UNKOWNERR,
				"error":str(e),
				"message":"未知错误",
			})


class UserQueryHotelResource(Resource):
	@classmethod
	def post(cls):
		parser = reqparse.RequestParser()
		parser.add_argument("Province", location="form", required=True, type=str, help="Province参数类型不正确或缺失")
		parser.add_argument("City", location="form", required=True, type=str, help="City参数类型不正确或缺失")
		parser.add_argument("Area", location="form", type=str, required=True, help="Area参数类型不正确或缺失")
		try:
			kwargs = parser.parse_args()
			kwargs = put_remove_none(**kwargs)

			res = HotelService.get(**kwargs)
			if res.get("code") != RET.OK:
				logger.error(res.get("data").get("error"))
				return jsonify({
					"code": res.get("code"),
					"error": res.get("data").get("error"),
					"message": res.get("message"),
				})

			dataParser = ['Province','City','Area','HotelID','HotelName','Phone','HotelLabels','HotelDist','HotelPicUrl']
			data = commons.to_dict_by_Model(res.get("data"), dataParser)

			logger.info(f"query {kwargs.get('Province')}-{kwargs.get('City')}-{kwargs.get('Area')} success")
			return jsonify({
				"code": RET.OK,
				"message": "查询成功",
				"data": data,
			})
		except BadRequest as e:
			logger.error(str(e))
			return jsonify({
				"code": RET.PARAMERR,
				"error": str(e),
				"message": "获取参数失败",
			})
		except Exception as e:
			logger.error(str(e))
			return jsonify({
				"code": RET.UNKOWNERR,
				"error": str(e),
				"message": "未知错误",
			})
