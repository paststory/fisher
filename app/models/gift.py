# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 15:06
# @Author  : yang
# @File    : gift.py
from flask import current_app
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, SmallInteger, desc, func
from sqlalchemy.orm import relationship

from app.models.base import db, Base
from app.models.wish import Wish
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
        return yushu_book.first

    # 因為這裡返回的是多個礼物，实例更多表示的是一个，所以改用类方法
    @classmethod
    def recent(cls):
        '''
        默认展示过去的捐赠的30本书籍
        按创建时间降序排列
        不能展示重复书籍
        :return:
        '''
        recent_gift = Gift.query.filter_by(launched = False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = cls.query.filter_by(launched = False, uid = uid).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        count_list = db.session.query(Wish.isbn, func.count(Wish.id)).filter(Wish.status == 1,
                                          Wish.launched == False,
                                          Wish.isbn.in_(isbn_list)).group_by(Wish.isbn).all()
        # 以字典的方式返回，会更容易表达清楚数据含义，这里不建议直接返回，没有标识的数据，使用字典还有一点是比较方便
        count_list = [{'isbn':w[0], 'count':w[1]}for w in count_list]
        return count_list