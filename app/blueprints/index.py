from flask import redirect, Blueprint
from flask_login import current_user


index_bp = Blueprint('index', __name__)


@index_bp.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated:
        return redirect('/shows')
    else:
        return redirect('/login')
