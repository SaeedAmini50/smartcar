# __init__.py
from flask import Flask
from .mydb import database

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dlskfjlkos sodijflsaiuro'
    app.config['DATABASE_CONFIG'] = database

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
