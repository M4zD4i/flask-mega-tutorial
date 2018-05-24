from app import myapp

@myapp.route('/')
@myapp.route('/index')
def index():
    return "Nice to meet you!"