from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()  # Verify that the table exists

    return app
