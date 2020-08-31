# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 15:34
# @Author  : yang
# @File    : secure.py
# 机密配置
DIALCT = "mysql"
DRIVER = "cymysql"
USERNAME = "xxx"
PASSWORD = "xxx"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "fisher"
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALCT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
# JSON_AS_ASCII = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
DEBUG = True
SECRET_KEY = 'TtInterestingButNotEasy'

# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '123456789@qq.com'
MAIL_PASSWORD = 'dcouglctdwsngjfg'