# -*- coding:utf-8 -*-
from flask import Flask
from tool.filter import FilterConverter
from .extensions import (
    db,
    csrf,
    photos
)
from config import config
from flask_uploads import configure_uploads
# from flask_sqlalchemy import SQLAlchemy



def crate_app(config_name):

    app = Flask(__name__)

    # with app.test_request_context():
    #     db.create_all()

    app.config.from_object(config[config_name])
    db.init_app(app)

    configure_uploads(app, photos)

    app.url_map.converters['get_num'] = FilterConverter

    # 注册蓝图
    from api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    from adminlte import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app



