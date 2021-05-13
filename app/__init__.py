from flask import Flask
from flask.helpers import url_for



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MisTortillas'
    
    #registrar lo blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/')

    return app