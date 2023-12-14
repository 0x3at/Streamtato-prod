from flask import Blueprint, redirect, url_for, current_app
from flask_login import logout_user, login_required, current_user


logout_bp = Blueprint('logout', __name__)


@logout_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    if current_user.is_authenticated:
        current_app.logger.info(f"User {current_user.username} logged out")
        logout_user()

    return redirect(url_for('login.login'))
