from flask import current_app, flash, render_template, redirect, url_for
from flask_login import login_required, current_user

from . import web

# from .. import login_manager
from ..models.base import db
from ..models.gift import Gift
from ..view_models.gift import MyGifts


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mime = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mime]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyGifts(gifts_of_mime, wish_count_list)
    return render_template('my_gifts.html', gifts = view_model.my_gifts)

@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.is_active and current_user.can_save_to_list(isbn):
        # 换一种方法，优化异常操作
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
        flash('已赠送成功，感谢鱼书赠书网站')
    else:
        flash('这本书已添加到捐赠清单或者已存在与心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



