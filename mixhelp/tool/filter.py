# -*- coding:utf-8 -*-
from werkzeug.routing import BaseConverter


# 自定义过滤器
class FilterConverter(BaseConverter):

    def __init__(self, url_map, *items):
        super(FilterConverter, self).__init__(url_map)
        self.regex = items[0]







