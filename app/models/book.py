# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 16:30
# @Author  : yang
# @File    : book.py
import json
from sqlalchemy import Column, String
from sqlalchemy import Integer
# from app.models.base import Base
from app.models.base import db


class Book(db.Model):
    """
        一些属性定义重复性比较大，元类可以解决这个问题
    """
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    _author = Column('author', String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    @property
    def author(self):
        return self._author if not self._author else json.loads(self._author)

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            self._author = json.dumps(value, ensure_ascii=False)
        else:
            self._author = value

    @property
    def author_str(self):
        return '' if not self._author else '、'.join(self.author)