from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import url_for

#db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MisTortillas'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:GrupoVictor1@192.168.2.252/db_misFacturas'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    
    #db.init_app(app)

    #registrar lo blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/')

    return app
    