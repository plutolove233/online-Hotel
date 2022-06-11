#!/usr/bin/env python
# -*- coding:utf-8 -*-

import flask
from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.exceptions import BadRequest

from middlewares.JwtMiddleware import TokenRequire
from service.remarkService import RemarkService
from utils.myLogging import logger
from utils.response_code import RET
from utils.generate_id import GenerateID


class AddRemarkResource(Resource):
	@classmethod
	@TokenRequire
	def post(cls):
		parser = reqparse.RequestParser()
		parser.add_argument("RemarkContent", type=str, location="json", required=True)
		parser.add_argument("HotelID", type=int, location="json", required=True)
		try:
			temp = flask.g.user
			if temp.userType == 1:
				return jsonify({
					"code": RET.ROLEERR,
					"message": "用户无法使用该功能",
				})
			data = parser.parse_args()
			data['RemarkUserID'] = temp.userId
			data['RemarkID'] = int(GenerateID.create_random_id())
			res = RemarkService.add(**data)
			if res.get("code") != RET.OK:
				logger.error(res.get("data").get("error"))
				return jsonify({
					"code": res.get("code"),
					"error": res.get("data").get("error"),
					"message": res.get("message"),
				})

			logger.info("make remark success")
			return jsonify({
				"code": RET.OK,
				"message": "添加评论成功",
			})
		except BadRequest as e:
			logger.error(str(e))
			return jsonify({
				"code": RET.PARAMERR,
				"error": str(e),
				"message": "获取请求参数失败",
			})
		except Exception as e:
			logger.warning(str(e))
			return jsonify({
				"code": RET.UNKOWNERR,
				"error": str(e),
				"message": "未知错误",
			})


class GetAllRemarkInfoResource(Resource):
	@classmethod
	def get(cls):
		parser = reqparse.RequestParser()
		parser.add_argument("HotelID", type=int, location="json", required=False)
		try:
			data = parser.parse_args()
			res = RemarkService.GetHotelRemark(**data)
			if res.get("code") != RET.OK:
				logger.error(res.get("error"))
				return jsonify(res)
			logger.info("get remark info success")
			return jsonify(res)
		except BadRequest as e:
			logger.error(str(e))
			return jsonify({
				"code": RET.PARAMERR,
				"error": str(e),
				"message": "获取请求参数失败",
			})
		except Exception as e:
			logger.warning(str(e))
			return jsonify({
				"code": RET.UNKOWNERR,
				"error": str(e),
				"message": "未知错误",
			})


class DeleteRemarkResource(Resource):
	@classmethod
	@TokenRequire
	def delete(cls):
		parser = reqparse.RequestParser()
		parser.add_argument("RemarkID", location="json", type=int, required=True)
		try:
			data = parser.parse_args()
			temp = flask.g.user
			if temp.userType == 1:
				return jsonify({
					"code": RET.ROLEERR,
					"message": "用户无法使用该功能",
				})
			res = RemarkService.get(**data)
			if res.get("code") != RET.OK:
				logger.error(res.get("data").get("error"))
				return jsonify({
					"code": res.get("code"),
					"error": res.get("data").get("error"),
					"message": res.get("message")
				})

			info = res.get("data")
			if info[0].get("RemarkUserID") != temp.userId:
				return jsonify({
					"code": RET.REQERR,
					"message": "用户不可删除其他用户评论",
				})

			res = RemarkService.delete(**data)
			if res.get("code") != RET.OK:
				logger.error(res.get("data").get("error"))
				return jsonify({
					"code": res.get("code"),
					"error": res.get("data").get("error"),
					"message": res.get("message")
				})
			logger.info("delete remark success")
			return jsonify({
				"code": RET.OK,
				"message": "删除成功",
			})
		except BadRequest as e:
			logger.error(str(e))
			return jsonify({
				"code": RET.PARAMERR,
				"error": str(e),
				"message": "获取请求参数失败",
			})
		except Exception as e:
			logger.warning(str(e))
			return jsonify({
				"code": RET.UNKOWNERR,
				"error": str(e),
				"message": "未知错误",
			})
