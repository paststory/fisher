# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 12:45
# @Author  : yang
# @File    : lifeCycle.py
from flask import request, current_app

from . import web

@web.route('/lifecycle')
def life(self):
    req = request
    app = current_app

    pass