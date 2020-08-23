# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 15:05
# @Author  : yang
# @File    : user.py
from flask import current_app
from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, func
from sqlalchemy import String, Unicode, DateTime, Boolean
from sqlalchemy import SmallInteger, Integer, Float
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import login_manager
from app.libs.helper import is_isbn_or_key
from app.models.base import db, Base
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class User(UserMixin,Base):
    __tablename__ = 'user'
    # __bind_key__ = 'fisher'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    # gifts = relationship('Gift')

    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        # 加密的一种方法
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 判断当前用户捐献以及心愿里没有当前这本书
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False

    # 生成token
    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        user = User.query.get(data.get('id'))
        if user is None:
            return False
        user.password = new_password
        db.session.commit()
        return True

    # flask_login 默认需要的函数，用了获取实体类对象的唯一标示
    # 这里通过继承的方式，不在需要重写
    # def get_id(self):
    #     return self.id

# print(a)
@login_manager.user_loader
def get_user(user_id):
    return db.session.query(User).get(user_id)
# @login_manager.user_loader
# def get_user(uid):
#     return User.query.get(int(uid))
