from flask import render_template

from . import web
from ..models.gift import Gift
from ..view_models.book import BookViewModel


@web.route('/')
def index():
    # 面向对象，每个类的方法是非常清晰的，对象之间的方法调用，完成复杂的业务逻辑
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent = books)

@web.route('/personal')
def personal_center():
    pass
