import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'S0M353CR37K3Y'