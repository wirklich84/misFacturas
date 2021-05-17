from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo, Length, DataRequired, Email


class LoginForm(Form):
    email = StringField(label='Email', validators=[DataRequired('Campo requerido'), Email(message='No es un correo valido')])
    password = PasswordField(label='Password', validators=[DataRequired('Campo requerido')])
    submit = SubmitField(label='Login')


class SignupForm(Form):
    email = StringField(label='Email',validators=[DataRequired('Campo requerido'), Email(message='No es un correo valido')])
    name = StringField(label='Nombre', validators=[DataRequired('Campo requerido')])
    password = PasswordField(label='Password', validators=[DataRequired('Campo requerido')])
    confirm_password = PasswordField(label='Confirmar Password', validators=[DataRequired('Campo requerido'), EqualTo('password',  message='No son iguales las contraseñas')])
    submit = SubmitField(label='Registrar')