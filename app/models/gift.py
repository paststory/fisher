# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 15:06
# @Author  : yang
# @File    : gift.py
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, SmallInteger
from sqlalchemy.orm import relationship

from app.models.base import db, Base
from app.spider.yushu_book import YuShuBook


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

    def is_yourself_gift(self, uid):
        if self.uid == uid:
            return True

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book