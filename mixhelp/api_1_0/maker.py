# -*- coding:utf-8 -*-
from . import api
import logging
from flask import render_template
from flask import request,jsonify,g
from mixhelp.models.problem import Problem_SPU, Problem_SKU, ProblemType


# 问题中心首页
@api.route('/makers/first', methods=['GET', 'POST'])
def first_page():
    # 获取所有问题类的对象
    try:
        type_data = ProblemType.query.all()
    except Exception as e:
        logging.error(e)

    g.type_data = type_data

    return render_template('index.html', type=type_data)


# 分组问题页面
@api.route('/makers/second')
def second_page():

    type_name = request.form.get('type_name')

    if type_name is None:
        return jsonify({'result': '该问题不存在'})

    try:
        type_data = ProblemType.query.filter_by(type_name=type_name).get()
    except Exception as e:
        logging.error(e)

    try:
        spu_data = Problem_SPU.query.filter_by(spu_id=type_data.id).all()
    except Exception as e:
        logging.error(e)

    data = {
        'spu' == spu_data,
        'type' == g.type_data
    }
    return render_template('',data=data)

# 详情问题页








