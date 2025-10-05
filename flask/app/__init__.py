from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@{host}:{port}/{database}'.format(
        username=os.environ['POSTGRES_USERNAME'],
        password=os.environ['POSTGRES_USERNAME_PASSWORD'],
        port=os.environ['POSTGRES_PORT'],
        database=os.environ['POSTGRES_DB_NAME'],
    )

    # connect the app to the database
    db.init_app(app)

    from app.views.main import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    return app

