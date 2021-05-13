from flask import render_template

from . import auth_bp
from .forms import LoginForm

@auth_bp.route('/')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)