#setting up Flask Application

#import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#define database object db
db = SQLAlchemy()
DB_NAME = 'database.db'

#clases
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ASDMKMSKNOiejfewiknfi02309j2ifsdDFSDGWMP2M0-k23'
    #telling __init__.py file where the SQLAlchemy it's located
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #register Blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #create and verify the database after running app
    from .models import User, Note
    create_database(app)

    # logging manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

#creating the database if not exits
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Database Created Successfully')
