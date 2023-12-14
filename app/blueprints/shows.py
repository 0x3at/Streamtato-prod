from flask import Blueprint, redirect, url_for, request, render_template, flash, current_app
from flask_login import current_user, login_required
from app.models import DatabaseInterface


shows_bp = Blueprint('shows', __name__)


@shows_bp.route('/shows', methods=['GET', 'POST'])
@login_required
def shows():
    shows = DatabaseInterface.get_all_show_names()
    if request.method == 'GET':
        return render_template('shows.html', shows=shows, user=current_user)

    if request.method == 'POST':
        show = request.form.get('showname')
        return redirect(url_for('watch.watch', show=show))

    else:
        current_app.logger.warning(
            f"Invalid request method: {request.method} when requesting /shows endpoint")
        flash('Invalid request method.')
        return redirect(url_for('shows.shows'))
