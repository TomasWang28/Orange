from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
from cfg import Config
from flask_session import Session


sess = Session()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'



def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    sess.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)

    return app