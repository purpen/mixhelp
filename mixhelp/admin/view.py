# -*- coding:utf-8 -*-
import os
import logging
from flask import request, render_template, jsonify, redirect, url_for

from . import admin
from manager import app
from mixhelp.extensions import db
from mixhelp.models.issue import Classify, Info


@admin.route('/index')
def admin_index():

    try:
        classify_data = Classify.query.filter(Classify.pid == None).all()
    except Exception as e:
        logging.error(e)

    return render_template('admin.html', datas=classify_data)


@admin.route('/remove/<int:num>')
def remove_issue(num):
    try:
        classify_data = Classify.query.filter(Classify.id == num).first()
    except Exception as e:
        logging.error(e)

    try:
        second_classify_data = Classify.query.filter(classify_data.id == Classify.pid).first()
    except Exception as e:
        logging.error(e)

    try:
        info_data = Info.query.filter(second_classify_data.id == Info.id).first()
    except Exception as e:
        logging.error(e)

    try:
        db.session.delete(info_data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(e)
    try:
        db.session.delete(second_classify_data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(e)
    try:
        db.session.delete(classify_data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(e)

    return redirect(url_for('html.admin_index'))


@admin.route('/add_issue')
def index():

    try:
        classify_data = Classify.query.filter(Classify.pid == None).all()
    except Exception as e:
        logging.error(e)
    try:
        list_data = Classify.query.filter(Classify.pid != 0).all()
    except Exception as e:
        logging.error(e)

    data = {
        'classify': classify_data,
        'list': list_data
    }
    return render_template('add_issue.html', datas=data)


@admin.route('/add', methods=['POST'])
def add_issue_info():

    first_rank_name = request.form.get('first_classify')
    if not first_rank_name:
        return '问题种类不能为空'
    # 获取一级问题
    try:
        classify_data = Classify.query.filter(Classify.issue_name == first_rank_name).first()
    except Exception as e:
        logging.error(e)

    if classify_data is None:
        classify = Classify(issue_name=first_rank_name)

        try:
            db.session.add(classify)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(e)

    second_rank_name = request.form.get('second_classify')

    if not second_rank_name:
        return '二级问题不能为空'

    try:
        second_classify_data = Classify.query.filter(Classify.issue_name == second_rank_name).first()
    except Exception as e:
        logging.error(e)

    if second_classify_data is None:

        try:
            classify_data = Classify.query.filter(Classify.issue_name == first_rank_name).first()
        except Exception as e:
            logging.error(e)

        second_classify_data = Classify(issue_name=second_rank_name, pid=classify_data.id)

        try:
            db.session.add(second_classify_data)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(e)

    details_name = request.form.get('details_name')

    if not details_name:
        return '详情问题名称不能为空'

    try:
        info_data = Info.query.filter(Info.details_name == details_name).first()
    except Exception as e:
        logging.error(e)

    if info_data is None:
        details_title = request.form.get('details_title')
        content = request.form.get('content')

        info = Info(
            details_name=details_name,
            details_title=details_title,
            content=content,
            category_id=second_classify_data.id
        )

        try:
            db.session.add(info)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(e)

    return redirect(url_for('html.admin_index'))


@admin.route('/upload_image', methods=['POST', 'GET'])
def upload_img():

    if 'image_up' not in request.files:     # 没有发现图片数据
        return jsonify(message='没发现要上传的图片')
    file_metas = request.files['image_up']
    filename = file_metas.filename   # 获取图片名称
    file_metas.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))  # 存储图片到服务器
    return jsonify(message='success', url='/static/public/uploads/{0}'.format(filename))


@admin.route('/amend/<int:num>')
def amend_index(num):
    try:
        first_classify_data = Classify.query.filter(Classify.id == num).first()
    except Exception as e:
        logging.error(e)

    try:
        second_classify_data = Classify.query.filter(Classify.pid == first_classify_data.id).all()
    except Exception as e:
        logging.error(e)

    issue_info_list = []
    for data in second_classify_data:
        try:
            issue_info_data = Info.query.filter(data.id == Info.category_id).all()
            issue_info_list.append((data, issue_info_data))
        except Exception as e:
            logging.error(e)

    data = {
        'first_classify_data': first_classify_data,
        'second_classify_data': second_classify_data,
        'issue_info': issue_info_list
    }

    return render_template('amend_issue.html', datas=data)


@admin.route('/amend', methods=['POST'])
def amend():
    second_rank_name = request.form.get('second_classify')
    details_name = request.form.get('details_name')
    details_title = request.form.get('details_title')
    content = request.form.get('content')

    if not all([second_rank_name, details_name, details_title, content]):
        return '参数不全'

    try:
        classif_data = Classify.query.filter(Classify.issue_name == second_rank_name).first()
    except Exception as e:
        logging.error(e)

    if classif_data is None:
        return redirect(url_for('html.admin_index'))

    try:
        issue_info_data = Info.query.filter(classif_data.id == Info.category_id).first()
    except Exception as e:
        logging.error(e)

    issue_info_data.details_name = details_name
    issue_info_data.details_title = details_title
    issue_info_data.content = content

    try:
        db.session.add(issue_info_data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logging.error(e)
    return redirect(url_for('html.admin_index'))








