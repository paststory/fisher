# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 11:08
# @Author  : yang
# @File    : __init__.py

from flask import Flask

from app.models.book import db
from app.web import web


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    register_blueprints(app)
    db.init_app(app)
    # 方法一
    db.create_all(app=app)
    # 方法二
    # with app.app_context():
    #     db.create_all()
    return app

def register_blueprints(app):
    app.register_blueprint(web)