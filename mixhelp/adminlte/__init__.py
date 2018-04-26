# -*- coding:utf-8 -*-
from flask import Blueprint
admin = Blueprint('html', __name__)
from . import upload,index
