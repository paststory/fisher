from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from . import web
from ..models.base import db
from ..models.wish import Wish
from ..spider.yushu_book import YuShuBook
from ..view_models.wish import MyWishes


@web.route('/my/wish')
@login_required
def my_wish():
    uid = current_user.id
    wishes_of_mime = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wishes_of_mime]
    gift_count_list = Wish.get_gift_counts(isbn_list)
    view_model = MyWishes(wishes_of_mime, gift_count_list)
    return render_template('my_wish.html', wishes=view_model.my_wishes)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.uid = current_user.id
            wish.isbn = isbn
            db.session.add(wish)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
