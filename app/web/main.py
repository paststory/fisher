from . import web




@web.route('/')
def index():
    return 'hello'
    pass


@web.route('/personal')
def personal_center():
    pass
