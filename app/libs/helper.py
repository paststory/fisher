# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 11:47
# @Author  : yang
# @File    : helper.py

def is_isbn_or_key(word):
    """
    :param word: 查询参数
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_isbn = word.replace('_','')
    if '_' in word and len(short_isbn) == 10 and short_isbn.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key