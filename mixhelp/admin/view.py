# -*- coding:utf-8 -*-
import logging
from . import admin
from flask import request
from mixhelp.extensions import photos, db
from mixhelp.models.issue import Classify, Info


@admin.route('/set', methods=['POST'])
def set_info():

    type_name = request.form.get('content')
    print type_name
    if type_name is None:
        return '问题种类不能为空'
    try:
        classify_data = Classify.query.filter(Classify.type_name == type_name).first()
    except Exception as e:
        logging.error(e)

    if classify_data is None:
        classify = Classify(type_name=type_name)

        try:
            db.session.add(classify)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(e)

    group_name = request.form.get('group_name')

    if group_name is None:
        return '分组问题不能为空'

    try:
        group_data = Group.query.filter(Group.group_name == group_name).first()
    except Exception as e:
        logging.error(e)

    if group_data is None:

        group = Group(group_name=group_name, classify_id=type_name)

        try:
            db.session.add(group)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(e)

    # title = request.form.get('title')
    details_name = request.form.get('details_name')

    if details_name is None:
        return '详情问题不能为空'

    try:
        info_data = Info.query.filter(Info.details_name == details_name).first()
    except Exception as e:
        logging.error(e)

    if info_data is None:

    # 获取图片url
        if request.method == 'POST' and 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            image_url = photos.url(filename)
        else:
            return '图片上传失败'

        details_name = request.form.get('details_name')
        details_title = request.form.get('details_title')
        content = request.form.get('content')
        file_url = request.form.get('file_url')

        info = Info(
            details_name=details_name,
            details_title=details_title,
            content=content,
            image_url=image_url,
            file_url=file_url,
            info_name=group_name
        )

        try:
            db.session.add(info)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(e)

    return '上传成功'





