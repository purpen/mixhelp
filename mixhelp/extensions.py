# -*- coding:utf-8 -*-
# 数据库连接
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_uploads import UploadSet, IMAGES


db = SQLAlchemy()
csrf = CSRFProtect()
photos = UploadSet('photos', IMAGES)
