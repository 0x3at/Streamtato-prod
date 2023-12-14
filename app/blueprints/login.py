from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash
from app.models import DatabaseInterface

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = DatabaseInterface.get_user_by_username(username=username)
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category='success')
                login_user(user, remember=True)
                current_app.logger.info(f"User {username} logged in")
                return redirect(url_for('shows.shows'))
            else:
                flash("Incorrect Password, try again.", category='error')
                current_app.logger.info(
                    f"User {username} entered incorrect password")
        else:
            current_app.logger.info(
                f"User {username} does not exist, but was attempted to be signed into")
            flash("Incorrect Username, try again.", category='error')

    return render_template("login.html", user=current_user)
