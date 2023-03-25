from flask import Flask, jsonify, request
import models
from db import db
from flask_smorest import Api

def create_app():
		
	app = Flask(__name__, template_folder='templates')
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)

	# api = Api(app)

	with app.app_context():
		db.create_all()

	from controllers.userController import user_controller_bp
	from controllers.categoriaController import categoria_controller_bp
	from controllers.despesaController import despesa_controller_bp
	app.register_blueprint(user_controller_bp)
	app.register_blueprint(categoria_controller_bp)
	app.register_blueprint(despesa_controller_bp)

	@app.route('/')
	def index():
		return 'Hello World'

	return app



if __name__ == '__main__':
	app = create_app()
	app.run(debug=True)
