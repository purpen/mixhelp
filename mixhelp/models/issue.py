# -*- coding:utf-8 -*-
from mixhelp.extensions import db


class Classify(db.Model):
    """问题分类表"""

    __tablename__ = 'issue_classify'

    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(50), index=True)
    group = db.relationship('Group')


class Group(db.Model):
    """问题分组表"""

    __tablename__ = 'issue_group'

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), unique=True)
    classify_id = db.Column(db.String(50), db.ForeignKey('issue_classify.type_name'))
    info = db.relationship('Info')


class Info(db.Model):
    """信息表"""

    __tablename__ = 'issue_info'

    id = db.Column(db.Integer, primary_key=True)
    details_name = db.Column(db.String(50), index=True)
    details_title = db.Column(db.String(30))
    content = db.Column(db.Text)
    comment_num = db.Column(db.Integer)
    solve_num = db.Column(db.Integer)
    unsolved_num = db.Column(db.Integer)
    image_url = db.Column(db.String(200))
    file_url = db.Column(db.String(50))
    cause_describe = db.Column(db.Integer, default=0)
    cause_product = db.Column(db.Integer, default=0)
    cause_content_no = db.Column(db.Integer, default=0)
    cause_operation = db.Column(db.Integer, default=0)
    info_name = db.Column(db.String(50), db.ForeignKey('issue_group.group_name'))





