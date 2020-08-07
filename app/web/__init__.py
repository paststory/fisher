# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 11:50
# @Author  : yang
# @File    : __init__.py
from flask import Blueprint

web = Blueprint('web',__package__)

from app.web import book