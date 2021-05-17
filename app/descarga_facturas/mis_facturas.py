from flask import render_template
from . import mis_facturas_bp
from flask_login import login_user, login_required, logout_user, current_user


@mis_facturas_bp.route('/index', methods=['POST', 'GET'])
@login_required
def index():
    return render_template('descarga_facturas/home.html')
