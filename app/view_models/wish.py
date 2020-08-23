# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 17:29
# @Author  : yang
# @File    : wish.py
from .book import BookViewModel


class MyWishes:
    def __init__(self, wishes, gifts_count):
        self.my_wishes = []
        self.__parse(wishes, gifts_count)

    def __parse(self, wishes, gifts_count):
        my_wishes = []
        for wish in wishes:
            count = 0
            for gift_count in gifts_count:
                if wish.isbn == gift_count['isbn']:
                    count = gift_count['count']
            else:
                r = {
                    'wishes_count': count,
                    'book': BookViewModel(wish.book.first),
                    'id': wish.id
                }
                my_wishes.append(r)
        self.my_wishes = my_wishes


