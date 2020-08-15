# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 15:54
# @Author  : yang
# @File    : yushu_book.py
from app.libs.httpModule import HTTP
# 防止循环导入,获取flask核心对象
from flask import current_app

'''
面向对象思想
描述特征（类变量，实例变量）
行为（方法）
'''
class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.books = []
        self.total = 0

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    def search_by_isbn(self,isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)
        # return response


    def search_by_keyword(self,key,page=1):
        url = self.keyword_url.format(key,current_app.config['PER_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)
        # return response


    def calculate_start(self,page):
        return (page-1) * current_app.config['PER_PAGE']