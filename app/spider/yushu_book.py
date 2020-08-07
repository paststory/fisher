# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 15:54
# @Author  : yang
# @File    : yushu_book.py
from app.libs.httpModule import HTTP
# 防止循环导入,获取flask核心对象
from flask import current_app


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    per_page = 15

    @classmethod
    def search_by_isbn(cls,isbn):
        url = cls.isbn_url.format(isbn)
        response = HTTP.get(url)
        return response

    @classmethod
    def search_by_keyword(cls,key,page=1):
        url = cls.keyword_url.format(key,current_app.config['PER_PAGE'], cls.calculate_start(page))
        response = HTTP.get(url)
        return response

    @staticmethod
    def calculate_start(page):
        return (page-1) * current_app.config['PER_PAGE']