# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 11:50
# @Author  : yang
# @File    : __init__.py
from flask import Blueprint, render_template

web = Blueprint('web',__package__)

@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish