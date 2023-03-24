import os, random, string

class Config(object):
    CSRF_ENABLED = True
    SECRET = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' % (IP_HOST,PORT_HOST)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

app_config = {
    'development': DevelopmentConfig(),
    'testing': None,
    'production': None
}

app_active = os.getenv('FLASK_ENV')

if app_config is None:
    app_config = 'development'
                                   