from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from config import config_options
from flask_bootstrap import Bootstrap
# from . import db
db = SQLAlchemy()
DB_NAME = "database.db"



# Initializing Flask Extensions
bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)
     # Creating the app configurations
    app.config.from_object(config_options['development'])
    db.init_app(app)

    from .main.views import views
    from .auth.views import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')

    from .models import User, Pitch
    bootstrap.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://marial:Doralove91!@localhost/pitch_hub2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    return app
