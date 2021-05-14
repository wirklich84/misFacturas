from flask import render_template, request, redirect, url_for

from . import auth_bp
from .forms import LoginForm, SignupForm
from app import auth




@auth_bp.route('/', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data

        print(email)
    
    return render_template('auth/login.html', form=form)


@auth_bp.route('/home/<string:email>', methods=['POST', 'GET'])
def home(email):
    return render_template('auth/home.html', email=email)


@auth_bp.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    form = SignupForm(request.form)
    if request.method == 'POST':
        name = form.name.data
        email = form.email.data
        password = form.password.data

        print(name)

    return render_template('auth/sign-up.html', form=form)