# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 16:45
# @Author  : yang
# @File    : book.py
import json

from flask import request, render_template, url_for, flash

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
    else:
        flash('根据关键字搜索不到，请重新输入')
    return render_template('search_result.html', books=books)
        # return form.errors


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book = book, wishes = [], gifts = [])
    pass

@web.route('/book/htmlstudy')
def html():
    d1 = {
        'age':17,
        'name':'zhangsan'
    }
    d2 = {
        'gender':'nan',
        'phone':'135****8642'
    }
    flash('nihao,8yue')
    flash('here is a trouble', category='error')
    return render_template('test.html', d1=d1, d2=d2)