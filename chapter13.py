from app import myapp, db, cli
from app.models import User, Post


@myapp.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


