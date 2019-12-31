import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'my-secret')