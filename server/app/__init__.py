from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .config import Config
from .extensions import db, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS
    CORS(app, resources={
        r"/*": {
            "origins": ["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5000"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True
        }
    })

    db.init_app(app)
    jwt.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints
    from .routes.auth_routes import auth_bp
    from .routes.url_routes import url_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(url_bp, url_prefix="/url")

    return app
