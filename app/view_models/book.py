# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 19:27
# @Author  : yang
# @File    : book.py



class BookViewModel:
    def __init__(self, data):
        self.title = data['title']
        self.author = '、'.join(data['author'])
        self.publisher = data['publisher']
        self.image = data['image']
        self.price = data['price']
        self.summary = data['summary']
        self.isbn = data['isbn']
        self.pages = data['pages']

    @property
    def intro(self):
        intros = filter(lambda x : True if x else False,
                        [self.author,self.publisher,self.price])
        return '/'.join(intros)

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = None

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keyword = keyword

class _BookViewModel:
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

