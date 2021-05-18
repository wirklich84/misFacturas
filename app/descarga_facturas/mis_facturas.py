from flask import render_template
from . import mis_facturas_bp
from flask_login import login_user, login_required, logout_user, current_user
from .forms import FielForm
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_uploads import UploadSet, configure_uploads, DATA

cerfile = UploadSet('cerfile', ('cer',))


@mis_facturas_bp.route('/index', methods=['POST', 'GET'])
@login_required
def index():
    return render_template('descarga_facturas/home.html', usuario=current_user)

@mis_facturas_bp.route('/upload-fiel', methods=['GET', 'POST'])
@login_required
def upload_fiel():
    form = FielForm()
    if form.validate_on_submit():
        cerfile.save(form.file_cer.data)

    return render_template('descarga_facturas/upload_fiel.html',form=form, usuario=current_user)
