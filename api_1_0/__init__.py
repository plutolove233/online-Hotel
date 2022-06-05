#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .apiVersionResource import apiversion_blueprint
from .hotelResource import hotel_blueprint
from .orderFormResource import orderform_blueprint
from .remarkResource import remark_blueprint
from .roomResource import room_blueprint
from .roomTypeResource import roomtype_blueprint
from .userResource import user_blueprint


def init_router(app):
    from api_1_0.apiVersionResource import apiversion_blueprint
    app.register_blueprint(apiversion_blueprint, url_prefix="/api_1_0")

    # hotel blueprint register
    from api_1_0.hotelResource import hotel_blueprint
    app.register_blueprint(hotel_blueprint, url_prefix="/api_1_0")
    
    # orderForm blueprint register
    from api_1_0.orderFormResource import orderform_blueprint
    app.register_blueprint(orderform_blueprint, url_prefix="/api_1_0")
    
    # remark blueprint register
    from api_1_0.remarkResource import remark_blueprint
    app.register_blueprint(remark_blueprint, url_prefix="/api_1_0")
    
    # room blueprint register
    from api_1_0.roomResource import room_blueprint
    app.register_blueprint(room_blueprint, url_prefix="/api_1_0")
    
    # roomType blueprint register
    from api_1_0.roomTypeResource import roomtype_blueprint
    app.register_blueprint(roomtype_blueprint, url_prefix="/api_1_0")
    
    # user blueprint register
    from api_1_0.userResource import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix="/api_1_0")

    # login blueprint register
    from api_1_0.apiLoginResource import login_blueprint
    app.register_blueprint(login_blueprint, url_prefix='/api_1_0')
