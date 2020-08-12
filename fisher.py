# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 16:12
# @Author  : yang
# @File    : fisher.py
from app import create_app

app = create_app()




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=81,debug=app.config['DEBUG'], threading = True)