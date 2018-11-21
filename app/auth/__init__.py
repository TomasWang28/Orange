from flask import Blueprint

# main = Blueprint('main', __name__, template_folder='pages')
auth = Blueprint('auth', __name__)


from . import views