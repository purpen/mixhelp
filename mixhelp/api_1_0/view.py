# -*- coding:utf-8 -*-
from mixhelp.api_1_0 import api
import logging
from flask import render_template, jsonify, request, redirect, url_for

from mixhelp.models.issue import Info, Classify


# @api.route('/list_info/<name>')
# def issue_list_info():
#
#     message = request.args.get('name')
#     return redirect(url_for('api.issue_list', name=message))


@api.route('/list/<name>', methods=['GET', 'POST'])
def issue_list(name):

    try:
        classify_data = Classify.query.all()
    except Exception as e:
        logging.error(e)

    try:
        info_data = Info.query.filter(name == Info.info_name).all()
    except Exception as e:
        logging.error(e)

    data = {
        'type': classify_data,
        'info': info_data,
        'name': name
    }

    return render_template('issue_list.html', datas=data)


@api.route('/info/<name>', methods=['GET', 'POST'])
def issue_info(name):

    try:
        classify_data = Classify.query.all()
    except Exception as e:
        logging.error(e)

    try:
        info_data = Info.query.filter(Info.details_name == name).first()
    except Exception as e:
        logging.error(e)

    # if info_data is None:
    #     return jsonify({'res': 0, 'msg': '没有问题列表'})
    # print info_data
    data = {
        'type': classify_data,
        'info': info_data
    }

    return render_template('details.html', datas=data)






