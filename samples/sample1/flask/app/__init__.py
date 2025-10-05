from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@{host}:{port}/{database}'.format(
        username=os.environ['USERNAME'],
        password=os.environ['PASSWORD'],
        database=os.environ['DB_NAME'],
        host=os.environ['HOSTNAME'],
        port=os.environ['PORT'],
    )

    # connect the app to the database
    db.init_app(app)

    from app.views.main import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    return app


