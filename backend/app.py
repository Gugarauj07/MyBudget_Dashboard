from flask import Flask, jsonify, request
import datetime
from flask_sqlalchemy import SQLAlchemy
from config import app_config

config = app_config['development']

def create_app(config_name):
	app = Flask(__name__, template_folder='templates')
	app.secret_key = config.SECRET
	app.config.from_object(app_config['development'])
	app.config.from_pyfile('config.py')
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db = SQLAlchemy(app)
	db.init_app(app)

	@app.route('/')
	def index():
		return 'Hello World'
	
	from controllers.userController import user_controller_bp
	app.register_blueprint(user_controller_bp)

	return app

# x = datetime.datetime.now()

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# from controllers.userController import user_controller_bp
# app.register_blueprint(user_controller_bp)

# if __name__ == '__main__':
# 	app.run(debug=True)
