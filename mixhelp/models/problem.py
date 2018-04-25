# -*- coding:utf-8 -*-
from mixhelp.extensions import db


class Classify(db.Model):
    """问题分类表"""

    __tablename__ = 'classify'

    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(50), index=True, unique=True)
    group = db.relationship('Group')


class Group(db.Model):
    """问题分组表"""

    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), unique=True, index=True)
    classify_id = db.Column(db.String(50), db.ForeignKey('classify.type_name'))
    info = db.relationship('Info')


class Info(db.Model):
    """信息表"""

    __tablename__ = 'info'

    id = db.Column(db.Integer, primary_key=True)
    details_name = db.Column(db.String(50), unique=True, index=True)
    details_title = db.Column(db.String(30))
    content = db.Column(db.String(300))
    comment_num = db.Column(db.Integer)
    solve_num = db.Column(db.Integer)
    unsolved_num = db.Column(db.Integer)
    image_url = db.Column(db.String(50))
    file_url = db.Column(db.String(50))
    unsolved_cause = db.Column(db.Integer)
    info_name = db.Column(db.String(50), db.ForeignKey('group.group_name'))





