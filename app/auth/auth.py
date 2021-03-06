from flask import render_template, request, redirect, url_for
from flask.helpers import flash
from app import db 
from app.models import User
from . import auth_bp
from .forms import LoginForm, SignupForm
from app import auth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user




@auth_bp.route('/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():

        usuario = User.query.filter_by(email=form.email.data).first()

        if usuario:
            if check_password_hash(usuario.password , form.password.data):
                flash('Usuario logeado satisfactoriamente!!', category='success')
                login_user(usuario, remember=True)
                return redirect(url_for('mis_facturas.index'))
            else:
                flash('Password incorecto', category='error')
        else:
            flash('El usuario no existe', category='error')
    
    return render_template('auth/login.html', form=form, usuario = current_user)


@auth_bp.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('auth/home.html')


@auth_bp.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():

        usuario = User.query.filter_by(email=form.email.data).first()

        if usuario:
            flash(f'El correo: {form.email.data} ya esta registrao!', category='error')
        else:
            nuevo_usuario = User(form.email.data, generate_password_hash(form.password.data,  method='sha256'),form.name.data)
            db.session.add(nuevo_usuario)
            db.session.commit()
            usuario = User.query.filter_by(email={form.email.data}).first()
            login_user(usuario, remember=True)
            flash(f'Usuario creado satisfactoriamente!! {form.name.data}', 'success')
            return redirect(url_for('mis_facturas.index'))       

    return render_template('auth/sign-up.html', form=form, usuario = current_user)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))