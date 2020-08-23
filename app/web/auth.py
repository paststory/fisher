from flask import render_template, request, redirect, url_for, flash

from . import web


from ..forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from ..models.base import db
from ..models.user import User
from flask_login import login_user, logout_user, current_user


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
    if request.method == 'POST':
        form = EmailForm(request.form)
        if form.validate():
            account_email = form.email.data
            # first_or_404 没查找到结果，直接返回
            user = User.query.filter_by(email=account_email).first_or_404()
            from app.libs.email import send_test,send_email
            # send_test()
            send_email(form.email.data, '重置你的密码',
                       'email/reset_password', user=user,
                       token=user.generate_token())
            flash('一封邮件已发送到邮箱' + account_email + '，请及时查收')
            return redirect(url_for('web.login'))
    return render_template('auth/forget_password_request.html')


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    if not current_user.is_anonymous:
        return redirect(url_for('web.index'))
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        result = User.reset_password(token, form.password1.data)
        if result:
            flash('你的密码已更新,请使用新密码登录')
            return redirect(url_for('web.login'))
        else:
            return redirect(url_for('web.index'))
    return render_template('auth/forget_password.html')


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))
