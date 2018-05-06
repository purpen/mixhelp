# -*- coding:utf-8 -*-
from mixhelp.extensions import db


class Classify(db.Model):
    """问题分类表"""

    __tablename__ = 'issue_classify'

    id = db.Column(db.Integer, primary_key=True)
    issue_name = db.Column(db.String(50), index=True)
    pid = db.Column(db.Integer, db.ForeignKey('issue_classify.id'))
    info = db.relationship('Info', backref=db.backref('classify'))


class Info(db.Model):
    """问题分组表"""

    __tablename__ = 'issue_info'

    id = db.Column(db.Integer, primary_key=True)
    details_name = db.Column(db.String(50), index=True)
    details_title = db.Column(db.String(50))
    content = db.Column(db.Text)
    comment_num = db.Column(db.Integer, default=0)
    solve_num = db.Column(db.Integer, default=0)
    unsolved_num = db.Column(db.Integer, default=0)
    cause_describe = db.Column(db.Integer, default=0)
    cause_product = db.Column(db.Integer, default=0)
    cause_content_no = db.Column(db.Integer, default=0)
    cause_operation = db.Column(db.Integer, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('issue_classify.id'))












