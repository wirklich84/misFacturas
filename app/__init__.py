from flask import Flask


def create_app():
    app = Flask(__name__)

    #registrar lo blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)


    return app