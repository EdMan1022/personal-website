import os


class BaseConfig(object):

    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):

    DEBUG = True

    pass


class TestConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True
