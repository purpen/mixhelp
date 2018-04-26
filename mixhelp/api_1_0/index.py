# -*- coding:utf-8 -*-
from . import api
import logging
from flask import render_template, g

from mixhelp.models.problem import Classify, Group, Info


@api.route('/index', methods=['GET'])
def index():

    try:
        classify_data = Classify.query.all()
    except Exception as e:
        logging.error(e)

    for data in classify_data:
        try:
            group_data = Group.query.filter(Group.classify_id == data.type_name).all()
            g.group_data = group_data
            break
        except Exception as e:
            logging.error(e)
    print 2
    try:
        info_data = Info.query.filter(g.group_data.group_name == Info.info_name).all()
        g.info_data = info_data
    except Exception as e:
        logging.error(e)


    if g.info_data is None:
        print 1
    else:
        for data in g.info_data:
            print data.details_name

    data = {
        'type': classify_data,
        # 'group': issue_group,
        'info': g.info_data
    }

    return render_template('index.html', datas=data)











