# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 15:05
# @Author  : yang
# @File    : user.py
from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, func
from sqlalchemy import String, Unicode, DateTime, Boolean
from sqlalchemy import SmallInteger, Integer, Float
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

# from app import login_manager
from app.models.base import db, Base


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

    # flask_login 默认需要的函数，用了获取实体类对象的唯一标示
    # 这里通过继承的方式，不在需要重写
    # def get_id(self):
    #     return self.id

# print(a)
# @login_manager.user_loader
# def get_user(user_id):
#     return db.session.query(User).get(user_id)
