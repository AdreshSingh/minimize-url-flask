from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .extensions import db, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints
    from .routes.auth_routes import auth_bp
    from .routes.url_routes import url_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(url_bp, url_prefix="/url")

    return app
