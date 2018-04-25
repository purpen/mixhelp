# -*- coding:utf-8 -*-
import os
import logging
from logging.handlers import RotatingFileHandler

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():


    ASSETS_DEBUG = True

    # Examples:
    # mysql://<username>:<password>@<host>/<dbname>[?<options>]
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost/mixhelp'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    UPLOADED_PHOTOS_DEST = basedir + 'public/uploads'


class DevelopmentConfig(Config):
    DEBUG = True


class LoggingConfig(Config):

    logging.basicConfig(level=logging.DEBUG)  # 调试debug级
    file_log_handler = RotatingFileHandler("logs/logs", maxBytes=1024 * 1024 * 100, backupCount=10)
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    file_log_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_log_handler)


config = {
    'develop':DevelopmentConfig,
    'logging':LoggingConfig
}


