import sys
from app import create_app
from config import app_config, app_active

config = app_config['development']
config.APP = create_app('development')

if __name__ == '__main__':
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)
    reload(sys)