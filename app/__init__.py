from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

#b
db = SQLAlchemy()
# flask-migrate plugin
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # CORS
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
