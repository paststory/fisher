# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 15:06
# @Author  : yang
# @File    : base.py
from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, SmallInteger, Integer

class SQLAlchemy(_SQLAlchemy):
    # 使用简单的方法简化异常操作,内部必须为生成器
    @contextmanager
    def auto_commit(self):
        try:
            yield
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    # 如果存的为时间 那么可以使用 Default = datetime.传一个时间函数对线，不会出现这种问题
    # 类变量会在服务启动的时候就初始化，所以类变量会变成一个统一的时间
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        # 实例变量在需要的时候，才会初始化，符合现在的需求
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def delete(self):
        self.status = 0