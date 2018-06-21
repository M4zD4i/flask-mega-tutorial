from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler


myapp = Flask(__name__)
myapp.config.from_object(Config)

db = SQLAlchemy(myapp)
migrate = Migrate(myapp, db)

login = LoginManager(myapp)
login.login_view = 'login'

from app import routes, models, errors


if not myapp.debug:
    if myapp.config['MAIL_SERVER']:
        auth = None
        if myapp.config['MAIL_USERNAME'] or myapp.config['MAIL_PASSWORD']:
            auth = (myapp.config['MAIL_USERNAME'], myapp.config['MAIL_PASSWORD'])
        secure = None
        if myapp.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(myapp.config['MAIL_SERVER'], myapp.config['MAIL_PORT']),
            fromaddr='no-reply@' + myapp.config['MAIL_SERVER'],
            toaddrs=myapp.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        myapp.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/flask-mega-tutorial.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    myapp.logger.addHandler(file_handler)

    myapp.logger.setLevel(logging.INFO)
    myapp.logger.info('Microblog startup')