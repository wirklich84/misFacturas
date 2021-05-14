from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired


class LoginForm(Form):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')


class SignupForm(Form):
    email = StringField(label='Email', validators=[DataRequired()])
    name = StringField(label='Nombre', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Registrar')