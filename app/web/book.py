# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 16:45
# @Author  : yang
# @File    : book.py
import json

from flask import request

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from ..forms.book import SearchForm
from ..view_models.book import BookViewModel, BookCollection


@web.route('/book/search')
def search():
    """
    :param q: 普通关键字isbn
    :param page: 查询页数
    :return:
    """
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q,page = form.q.data.strip(), form.page.data
        # 判断是否是isbn搜索
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q,page=page)

        books.fill(yushu_book,q)
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return form.errors