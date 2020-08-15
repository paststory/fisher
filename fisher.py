# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 16:12
# @Author  : yang
# @File    : fisher.py
from flask import request

from app import create_app

app = create_app()

# class no_local:
#     pass
#
# local = no_local()
# local.a = 1
#
# @app.route('/hello')
# def search():
#     print(getattr(request,'a',None))
#     request.a = 2
#     print('*******')
#     print(local.a)
#     local.a = 2
#     print('*******')
#     return ''



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=81,debug=app.config['DEBUG'], threaded = True)