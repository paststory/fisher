# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 15:06
# @Author  : yang
# @File    : base.py
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)