from flask_login import login_required

from . import web
__author__ = '七月'

# from .. import login_manager


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'my gift'
    pass


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



