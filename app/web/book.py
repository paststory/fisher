# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 16:45
# @Author  : yang
# @File    : book.py
from flask import request

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from ..forms.book import SearchForm
from ..view_models.book import BookViewModel


@web.route('/book/search')
def search():
    """
    :param q: 普通关键字isbn
    :param page: 查询页数
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q,page = form.q.data.strip(), form.page.data
        # 判断是否是isbn搜索
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        else:
            result = YuShuBook.search_by_keyword(q,page=page)
            result = BookViewModel.package_collection(result, q)
        return result
    else:
        return form.errors