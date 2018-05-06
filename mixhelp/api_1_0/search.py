# -*- coding:utf-8 -*-
import logging
from mixhelp.api_1_0 import api
from flask import request, redirect, url_for, render_template

from mixhelp.models.issue import Info, Classify


@api.route('/search', methods=['POST', 'GET'])
def search():
    issue_data = request.form.get('issue')
    if not issue_data:
        return redirect(url_for('api.index'))

    try:
        classify_data = Classify.query.all()
    except Exception as e:
        logging.error(e)

    try:
        issue_info = Info.query.filter(Info.details_name.ilike('%' + issue_data + '%')).all()
    except Exception as e:
        logging.error(e)
    print issue_info
    if not issue_info:
        return redirect(url_for('api.search_failure', issue_data=issue_data))

    issue_count = Info.query.filter(Info.details_name.ilike('%' + issue_data + '%')).count()
    data = {
        'type': classify_data,
        'info': issue_info,
        'data': issue_data,
        'count':issue_count
    }

    return render_template('search_list.html', datas=data)


@api.route('/search/<issue_data>', methods=['POST', 'GET'])
def search_failure(issue_data):

    try:
        classify_data = Classify.query.all()
    except Exception as e:
        logging.error(e)

    data = {
        'type': classify_data,
        'issue_name': issue_data
    }

    return render_template('search_failure.html', datas=data)