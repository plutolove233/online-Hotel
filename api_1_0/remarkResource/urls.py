#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import remark_blueprint
from api_1_0.remarkResource.remarkResource import RemarkResource
from api_1_0.remarkResource.remarkOtherResource import AddRemarkResource, GetAllRemarkInfoResource, DeleteRemarkResource

api = Api(remark_blueprint)

api.add_resource(RemarkResource, '/remark/<RemarkID>', '/remark', endpoint='remark')
api.add_resource(AddRemarkResource, '/remark/add', endpoint="add")
api.add_resource(GetAllRemarkInfoResource, '/remark/getInfo', endpoint="getInfo")
api.add_resource(DeleteRemarkResource, '/remark/delete', endpoint="delete")