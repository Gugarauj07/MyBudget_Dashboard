from flask import Flask, jsonify, request
import models
from db import db

def create_app():
		
	app = Flask(__name__, template_folder='templates')
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)

	with app.app_context():
		db.create_all()

	import controllers

	app.register_blueprint(user_controller_bp)
	app.register_blueprint(categoria_controller_bp)
	app.register_blueprint(despesa_controller_bp)
	app.register_blueprint(receita_controller_bp)
	app.register_blueprint(meta_controller_bp)
	app.register_blueprint(investimento_controller_bp)

	@app.route('/')
	def index():
		return 'Hello World'

	return app



if __name__ == '__main__':
	app = create_app()
	app.run(debug=True)
