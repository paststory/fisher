from flask import flash, redirect, url_for, render_template, request
from flask_login import current_user, login_required

from . import web
from ..forms.book import DriftForm
from ..libs.email import send_email
from ..models.base import db
from ..models.drift import Drift
from ..models.gift import Gift


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    current_gift = Gift.query.get_or_404(gid)
    if current_gift.is_yourself_gift(current_user.id):
        flash('这本书是你自己的^_^, 不能向自己索要书籍噢')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))
    can = current_user.can_satisfied_wish()
    if not can:
        return render_template('not_enough_beans.html', beans=current_user.beans)
    # gifter = current_gift.user.summary
    drift_form = DriftForm(request.form)
    if request.method == 'POST':
        if drift_form.validate():
            save_a_drift(drift_form, current_gift)
            send_email(current_gift.user.email, '有人想要一本书', 'email/get_gift',
                       wisher=current_user,
                       gift=current_gift)
            return redirect(url_for('web.pending'))
    gifter = current_gift.user.summary
    return render_template('drift.html', gifter=gifter,
                           user_beans=current_user.beans, form={'recipient_name':{}})
    pass


@web.route('/pending')
def pending():
    pass


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass

def save_a_drift(drift_form, current_gift):
    # 1. 减少查询次数
    # 2. 交易记录本身就应该是历史记录，不应该动态改变
    with db.auto_commit():
        drift = Drift()
        drift_form.populate_obj(drift)
        drift.gift_id = current_gift.id
        drift.requester_id = current_user.id
        drift.requester_nickname = current_user.nickname
        drift.gifter_nickname = current_gift.user.nickname
        drift.gifter_id = current_gift.user.id
        drift.book_title = current_gift.book.title
        drift.book_author = current_gift.book.author_str
        drift.book_img = current_gift.book.image_large
        db.session.add(drift)
    pass