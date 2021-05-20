from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    from smarts.commands import db_manage_bp
    from smarts.errors import errors_bp
    from smarts.messages import messages_bp
    from smarts.auth import auth_bp
    app.register_blueprint(db_manage_bp)
    app.register_blueprint(errors_bp)
    app.register_blueprint(messages_bp, url_prefix='/api/v1')
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')

    return app
