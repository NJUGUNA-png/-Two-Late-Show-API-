from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from server.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, SECRET_KEY

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['JWT_SECRET_KEY'] = SECRET_KEY

    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

   
    from server.controllers.auth_controller import auth_bp
    from server.controllers.guest_controller import guest_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(guest_bp)

    # Root route
    @app.route('/')
    def home():
        return {'message': 'Late Show API is working'}

    return app