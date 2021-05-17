from flask import Blueprint

mis_facturas_bp = Blueprint('mis_facturas',__name__, template_folder='templates')

from . import mis_facturas