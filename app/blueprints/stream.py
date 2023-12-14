from flask import Blueprint, redirect, url_for, render_template, flash, current_app
from flask_login import current_user, login_required
from app.models import DatabaseInterface


stream_bp = Blueprint('stream', __name__)


@stream_bp.route('/stream/<string:video_id>', methods=['GET', 'POST'])
@login_required
def stream(video_id=None):
    if video_id == None:
        redirect(url_for('shows.shows'))
    media = DatabaseInterface.get_media_by_id(int(video_id))
    if not media:
        current_app.logger.warning(
            f"User {current_user.username} attempted to access video {video_id} but it does not exist")
        flash('The Video Could Not be Found, Administrators have been notifed.')
        redirect(url_for('shows.shows'))
    return render_template('stream.html', user=current_user, video=media)
