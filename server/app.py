import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from controllers import guest_bp, episode_bp, appearance_bp, auth_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(guest_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(appearance_bp)
app.register_blueprint(auth_bp)


@app.route('/')
def index():
    return make_response(jsonify({"message": "Late Show API is running 🎬"}), 200)

if __name__ == '__main__':
    app.run(debug=True, port=5555)