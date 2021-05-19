from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import url_for
from flask_login import LoginManager
from flask_uploads import configure_uploads
from app.descarga_facturas.mis_facturas import cerfile

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MisTortillas'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@127.0.0.1/db_misFacturas'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['UPLOADED_CERFILE_DEST'] = 'uploads'
    configure_uploads(app, cerfile)

    db.init_app(app)

    from .models import User

    create_db(app)   

    #registrar lo blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/')

    from .descarga_facturas import mis_facturas_bp
    app.register_blueprint(mis_facturas_bp,  url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Necesitas logearte para acceder a esta pagina'
    login_manager.login_message_category = 'error'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_db(app):
    db.create_all(app=app)
    print("Se creo la base de datos!!")
    