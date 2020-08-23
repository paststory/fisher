# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 11:08
# @Author  : yang
# @File    : __init__.py

from flask import Flask

from app.models.book import db
# from app.models.user import User
from flask_login import LoginManager
from flask_mail import Mail

login_manager = LoginManager()
mail = Mail()

# @login_manager.user_loader
# def load_user(user_id):
#     user = db.session.query(User).get(user_id)
#     return user

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    register_blueprints(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    # 没有登录的时候，跳转到的页面
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    # 方法一
    db.create_all(app=app)
    # 方法二
    # with app.app_context():
    #     db.create_all()
    return app

def register_blueprints(app):
    # 防止循环导入的出现
    from app.web import web
    app.register_blueprint(web)