# -*- coding:utf-8 -*-
from mixhelp.api_1_0 import api
import logging
from flask import render_template, g, request, redirect

from mixhelp.models.issue import Classify, Info


@api.route('/index', methods=['GET'])
def index():

    try:
        classify_data = Classify.query.all()
    except Exception as e:
        logging.error(e)

    for data in classify_data:
        try:
            group_data = Group.query.filter(Group.classify_id == data.type_name).first()
            g.group_data = group_data
        except Exception as e:
            logging.error(e)
        break

    data = {
        'type': classify_data,
        'group': g.group_data
    }

    return render_template('index.html', datas=data)


















