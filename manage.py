#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
   入口程序
"""
import os

import flask

from app import create_app
from flask_script import Manager, Server
from flask import request, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from utils.response_code import RET

# 创建flask的app对象
app = create_app("develop")

# 通过Flask-Script的Manager,Server接管Flask运行
manager = Manager(app)

# 关闭Debug模式
manager.add_command("runserver", Server(use_debugger=False))


# 创建全站拦截器，每个请求之后根据请求方法统一设置返回头
@app.after_request
def process_response(response):
    allow_cors = ['OPTIONS', 'PUT', 'DELETE', 'GET', 'POST']
    if request.method in allow_cors:
        response.headers["Access-Control-Allow-Origin"] = '*'
        if request.headers.get('Origin') and request.headers['Origin'] == 'http://api.onlineHotel.com':
            response.headers["Access-Control-Allow-Origin"] = 'http://api.onlineHotel.com'

        response.headers["Access-Control-Allow-Credentials"] = 'true'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,GET,POST,PUT,DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type,token,Authorization'
        response.headers['Access-Control-Expose-Headers'] = 'VerifyCodeID,ext'
    return response


if __name__ == "__main__":
    # print(app.url_map)
    manager.run()

