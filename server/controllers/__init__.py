from .auth_controller import auth_bp
from .guest_controller import guest_bp
from .episode_controller import episode_bp
from .appearance_controller import appearance_bp


def register_controllers(app):
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(guest_bp, url_prefix="/guests")
    app.register_blueprint(episode_bp, url_prefix="/episodes")
    app.register_blueprint(appearance_bp, url_prefix="/appearances")
