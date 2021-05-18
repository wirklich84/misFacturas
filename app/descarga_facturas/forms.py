from flask_wtf import Form
from flask_uploads import UploadSet, configure_uploads, DATA
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo, Length, DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

class FielForm(Form):
    file_cer = FileField(label='Archivo .cer', validators=[FileRequired(),
        FileAllowed(['cer'], 'Solo archivos .cer')])
    submit = SubmitField(label='Subir Archivos')