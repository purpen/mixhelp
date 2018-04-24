# -*- coding:utf-8 -*-
from mixhelp.extensions import db


class ProblemType(db.Model):
    """问题种类表"""

    __tablename__ = 'problem_type'

    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(50), index=True)


class Problem_SPU(db.Model):
    """分组问题表"""

    __tablename__ = 'problem_spu'

    id = db.Column(db.Integer, primary_key=True)
    spu_name = db.Column(db.String(50), index=True)
    sku_id = db.Column(db.Integer, db.ForeignKey('problem_type.id'))
    name = db.relationship('Problem_SKU', backref='sku')


class Problem_SKU(db.Model):
    """详细问题表"""

    __tablename__ = 'problem_sku'

    id = db.Column(db.Integer, primary_key=True)
    sku_name = db.Column(db.String(50), index=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(200))
    comment_num = db.Column(db.Integer)
    solve_num = db.Column(db.Integer)
    unsolve_num = db.Column(db.Integer)
    picture_url = db.Column(db.String(50))
    file_url = db.Column(db.String(50))
    problem_cause = db.Column(db.String(50))
    spu_id = db.Column(db.Integer, db.ForeignKey('problem_spu.id'))