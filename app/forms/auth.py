# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 15:33
# @Author  : yang
# @File    : auth.py
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo
import email_validator

from app.models.user import User


class RegisterForm(Form):
    nickname = StringField('昵称', validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    password = PasswordField('密码', validators=[
        DataRequired(), Length(6, 20)])

    email = StringField('电子邮件', validators={DataRequired(), Length(1, 64),
                                            Email(message='电子邮箱不符合规范')})

    # 会自动检测字段位为email是否符合要求
    def validate_email(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('电子邮箱已被注册')

class LoginForm(Form):
    password = PasswordField('密码', validators=[
        DataRequired(message='密码不可以为空，请输入你的密码')])
    email = StringField('电子邮件', validators={DataRequired(), Length(1, 64),
                                            Email(message='电子邮箱不符合规范')})
    # def validate_email(self,field):
    #     if User.query.filter_by(email = field.data).first():
    #         raise ValidationError('电子邮箱已被注册')

class EmailForm(Form):
    email = StringField('电子邮件', validators={DataRequired(), Length(1, 64),
                                            Email(message='电子邮箱不符合规范')})

class ResetPasswordForm(Form):
    password1 = PasswordField('新密码', validators=[
        DataRequired(), Length(6, 20, message='密码长度至少需要在6到20个字符之间'),
        EqualTo('password2', message='两次输入的密码不相同')])
    password2 = PasswordField('确认新密码', validators=[
        DataRequired(), Length(6, 20)])