# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 19:27
# @Author  : yang
# @File    : book.py
class BookViewModel:
    @classmethod
    def package_single(cls, data ,keyword):
        returned = {
            'keyword': keyword,
            'total': 0,
            'books': []
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data ,keyword):
        returned = {
            'keyword': keyword,
            'total': 0,
            'books': []
        }
        if data:
            # 使用数据源头提供的总数
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'author': '、'.join(data['author']),
            'binding': data['binding'] or '',
            'publisher': data['publisher'],
            'image': data['images']['large'],
            'price': data['price'],
            'isbn': data['isbn'],
            'pubdate': data['pubdate'],
            'summary': data['summary'] or '',
            'pages': data['pages'] or ''
        }
        return book

