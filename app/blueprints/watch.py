from flask import Blueprint, redirect, url_for, render_template, flash
from flask_login import current_user, login_required
from app.models import DatabaseInterface


watch_bp = Blueprint('watch', __name__)


@watch_bp.route('/watch/<string:show>', methods=['GET'])
@login_required
def watch(show=None):
    if show == None:
        flash('Please select a show!')
        redirect(url_for('shows.shows'))
    episodes = DatabaseInterface.get_sorted_episodes_by_show(show)
    if not episodes:
        flash('No episodes found for this show!')
        redirect(url_for('shows.shows'))
    return render_template('watch.html', episodes=episodes, user=current_user)
