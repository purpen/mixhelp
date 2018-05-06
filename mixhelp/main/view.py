# -*- coding:utf-8 -*-
import logging
from . import main
from flask import render_template, request, redirect, url_for, jsonify

from mixhelp.extensions import db
from mixhelp.models.issue import Classify, Info


def parent_template_data():
    global classify_data
    try:
        classify_data = Classify.query.filter(Classify.pid == None).all()
    except Exception as e:
        logging.error(e)

    issue_list = []
    for data in classify_data:
        try:
            son_data = Classify.query.filter(data.id == Classify.pid).all()
            issue_list.append((data, son_data))
        except Exception as e:
            logging.error(e)

    return issue_list


@main.route('/index', methods=['GET', 'POST'])
def index():

    classify_data = parent_template_data()

    try:
        first_classify_data = Classify.query.filter(Classify.pid == None).first()
    except Exception as e:
        logging.error(e)

    try:
        index_issue_list = Classify.query.filter(first_classify_data.id == Classify.pid).first()
    except Exception as e:
        logging.error(e)
    data = {
        'parent_data': classify_data,
        'navigation': first_classify_data,
        'index_issue': index_issue_list
    }

    return render_template('index.html', datas=data)


@main.route('/issue_info/<num>')
def issue_info(num):
    """问题详情页"""
    global first_navigation
    try:
        info_data = Info.query.filter(Info.id == num).first()
    except Exception as e:
        logging.error(e)
    try:
        first_navigation = Classify.query.filter(Classify.id == info_data.classify.pid).first()
    except Exception as e:
        logging.error(e)

    classify_data = parent_template_data()

    data = {
        'parent_data': classify_data,
        'info': info_data,
        'first_navigation': first_navigation
    }
    return render_template('issue_details.html', datas=data)


@main.route('/issue_list/<num>')
def issue_list(num):
    """问题列表页"""
    global first_navigation, first_navigation
    try:
        info_data = Info.query.filter(Info.category_id == num).all()
    except Exception as e:
        logging.error(e)

    try:
        second_navigation = Classify.query.filter(Classify.id == num).first()
    except Exception as e:
        logging.error(e)

    try:
        first_navigation = Classify.query.filter(second_navigation.pid == Classify.id).first()
    except Exception as e:
        logging.error(e)

    classify_data = parent_template_data()
    data = {
        'parent_data': classify_data,
        'info': info_data,
        'second_navigation': second_navigation,
        'first_navigation': first_navigation
    }

    return render_template('issue_list.html', datas=data)


@main.route('/search', methods=['POST', 'GET'])
def search():
    """搜索页"""
    issue_data = request.form.get('issue')
    if not issue_data:
        return redirect(url_for('main.index'))

    try:
        issue_info_data = Info.query.filter(Info.details_name.ilike('%' + issue_data + '%')).all()
    except Exception as e:
        logging.error(e)

    if not issue_info_data:
        return redirect(url_for('main.search_failure', issue_data=issue_data))

    issue_count = Info.query.filter(Info.details_name.ilike('%' + issue_data + '%')).count()

    classify_data = parent_template_data()
    data = {
        'parent_data': classify_data,
        'info': info_data,
        'data': issue_data,
        'count': issue_count
    }

    return render_template('search_list.html', datas=data)


@main.route('/search/<issue_data>', methods=['POST', 'GET'])
def search_failure(issue_data):
    """搜索错误页"""

    classify_data = parent_template_data()
    data = {
        'parent_data': classify_data,
        'issue_name': issue_data
    }

    return render_template('search_failure.html', datas=data)


@main.route('/comment_yes', methods=['POST'])
def comment_yes():

    num = request.form.get('num')

    try:
        issue_info_data = Info.query.filter(Info.id == num).first()
    except Exception as e:
        logging.error(e)
    issue_info_data.solve_num += 1
    issue_info_data.comment_num += 1

    try:
        db.session.add(issue_info_data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(e)
    return jsonify(res=0, message='评论成功')


@main.route('/comment_no', methods=['POST'])
def comment_no():
    num = request.form.get('num')

    try:
        info_data = Info.query.filter(Info.id == num).first()
    except Exception as e:
        logging.error(e)

    info_data.unsolved_num += 1
    info_data.comment_num += 1

    try:
        db.session.add(info_data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(e)

    return jsonify(res=0, message='评论成功')


@main.route('/issue_cause', methods=['GET', 'POST'])
def issue_case():
    global info_data
    issue_id = request.form.get('id')
    issue_cause = request.form.get('cause')
    issue_cause = int(issue_cause)

    try:
        info_data = Info.query.filter(Info.id == issue_id).first()
    except Exception as e:
        logging.error(e)

    if issue_cause == 1:
        info_data.cause_describe += 1
    elif issue_cause == 2:
        info_data.cause_product += 1
    elif issue_cause == 3:
        info_data.cause_content_no += 1
    elif issue_cause == 4:
        info_data.cause_operation += 1

    try:
        db.session.add(info_data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(e)

    return redirect(url_for('main.index'))


