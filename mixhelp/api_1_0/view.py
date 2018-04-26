# -*- coding:utf-8 -*-
from . import api
import logging
from flask import render_template, jsonify

from mixhelp.models.problem import Group, Info


@api.route('/issue/list/<name>', methods=['GET'])
def issue_group(name):

    try:
        issue_group = Group.query.filter(Group.group_name == name).all()
    except Exception as e:
        logging.error(e)

    return render_template('index.thml', issue_group=issue_group)


@api.route('/issue/info/<name>', methods=['GET'])
def issue_info(name):

    try:
        issue_info = Info.query.filter(Info.content == name).all()
    except Exception as e:
        logging.error(e)

    return render_template('index.thml', issue_info=issue_info)


