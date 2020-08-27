# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 19:17
# @Author  : yang
# @File    : email.py
from threading import Thread
from flask import current_app, render_template
from flask_mail import Message,Mail

mail = Mail()


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_email(to, subject, template, **kwargs):
    # current_app 为代理对象，每个线程中都会动态的重新赋值
    # 这里获取app的实例对象，就不会出现这种问题
    # 不然会报错 working outside of application context
    app = current_app._get_current_object()
    msg = Message('[鱼书]' + ' ' + subject,
                  sender=app.config['MAIL_USERNAME'], recipients=[to])
    # msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

def send_test():
    msg = Message('测试邮件', sender='1175019761@qq.com', body='Test', recipients=['1175019761@qq.com'])
    mail.send(msg)
    pass

if __name__ == '__main__':
    send_test()



