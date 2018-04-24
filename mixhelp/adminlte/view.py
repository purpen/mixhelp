# -*- coding:utf-8 -*-
from . import admin
from flask import request
from flask import render_template


@admin.route('/index')
def index():
    return render_template('admin.html')


@admin.route('/set', methods=['POST'])
def set_info():
    type_name = request.form.get('type_name')

    return type_name
