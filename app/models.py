from app import db 
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    nombre = db.Column(db.String(300))
    cer_file = db.Column(db.String(100), nullable=True)
    key_file = db.Column(db.String(100), nullable=True)
    pass_fiel = db.Column(db.String(100), nullable=True)

    def __init__(self, email, passsword, nombre, cer_file, key_file, pass_fiel):
        self.email = email
        self.password = passsword
        self.nombre = nombre
        self.cer_file = cer_file
        self.key_file = key_file
        self.pass_fiel = pass_fiel