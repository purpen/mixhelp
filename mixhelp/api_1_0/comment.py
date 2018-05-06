# -*- coding:utf-8 -*-
from mixhelp.api_1_0 import api
import logging
from flask import request, redirect, url_for

from mixhelp.extensions import db
from mixhelp.models.issue import Info


@api.route('/comment_yes', methods=['POST'])
def comment_yes():
    issue_data = request.form.get('title')

    try:
        info_data = Info.query.filter(Info.details_title == issue_data).first()
    except Exception as e:
        logging.error(e)

    if info_data.solve_num is None:
        info_data.solve_num = 0
    if info_data.comment_num is None:
        info_data.comment_num = 0
    info_data.solve_num += 1
    info_data.comment_num += 1

    try:
        db.session.add(info_data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(e)

    return '{"errno":0, "errmsg":"设置成功"}'


@api.route('/comment_no', methods=['POST'])
def comment_no():
    issue_data = request.form.get('title')

    try:
        info_data = Info.query.filter(Info.details_title == issue_data).first()
    except Exception as e:
        logging.error(e)

    if info_data.unsolved_num is None:
        info_data.unsolved_num = 0
    if info_data.comment_num is None:
        info_data.comment_num = 0
    info_data.unsolved_num += 1
    info_data.comment_num += 1

    try:
        db.session.add(info_data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(e)

    return '{"errno":0, "errmsg":"设置成功"}'


@api.route('/issue_cause', methods=['GET', 'POST'])
def issue_case():
    issue_title = request.form.get('title')
    issue_data = request.form.get('cause')
    issue_data = int(issue_data)

    try:
        info_data = Info.query.filter(Info.details_title == issue_title).first()
    except Exception as e:
        logging.error(e)

    if issue_data == 1:
        info_data.cause_describe += 1
    elif issue_data == 2:
        info_data.cause_product += 1
    elif issue_data == 3:
        info_data.cause_content_no += 1
    elif issue_data == 4:
        info_data.cause_operation += 1

    try:
        db.session.add(info_data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(e)

    return redirect(url_for('api.index'))



