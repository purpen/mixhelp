# -*- coding:utf-8 -*-
import logging
from . import admin
from flask import request
from flask import render_template
from mixhelp.extensions import photos, db
from mixhelp.models.problem import Classify, Group,Info


@admin.route('/index')
def index():
    return render_template('admin.html')


@admin.route('/set', methods=['POST'])
def set_info():

    type_name = request.form.get('type_name')
    if type_name is not None:

        classify = Classify(type_name=type_name)

        try:
            db.session.add(classify)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(e)

        return '问题种类不能为空'

    group_name = request.form.get('group_name')
    if group_name is not None:
        group = Group(group_name=group_name, classify=type_name)

        try:
            db.session.add(group)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(e)

        return '分组问题不能为空'

    title = request.form.get('title')
    details_name = request.form.get('details_name')

    # 获取图片url
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        image_url = photos.url(filename)

    details_name = request.form.get('details_name')
    details_title = request.form.get('details_title')
    content = request.form.get('content')
    file_url = request.form.get('file_url')

    info = Info(
        details_name=details_name,
        details_title=details_title,
        content=content,
        image_url=image_url,
        file_url=file_url
    )

    try:
        db.session.add(info)
        db.session.commit()
    except Exception as e:
        db.rollback()

    return '上传成功'





