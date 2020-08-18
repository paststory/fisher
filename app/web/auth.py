from flask import render_template, request, redirect, url_for, flash

from . import web


from ..forms.auth import RegisterForm, LoginForm
from ..models.base import db
from ..models.user import User
from flask_login import login_user

@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
        pass
    return render_template('auth/register.html', form=form)
    pass


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email = form.data['email']).first()
        if user and user.check_password(form.data['password']):
            login_user(user)
            next = request.args.get('next')
            # 防止跨站脚本攻击
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或者密码有误')
    return render_template('auth/login.html',form = form)
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
