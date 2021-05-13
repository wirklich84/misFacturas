from wtforms import Form, StringField, PasswordField, SubmitField


class LoginForm(Form):
    email = StringField(label='Email')
    password = PasswordField(label='Password')
    subtmit = SubmitField(label='Login')