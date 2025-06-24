from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import SQLALCHEMY_DATABASE_URI, JWT_SECRET_KEY, SQLALCHEMY_TRACK_MODIFICATIONS
from server.models import db
from server.controllers import register_controllers

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)
    migrate.init_app(app, db)
    JWTManager(app)

    register_controllers(app)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)