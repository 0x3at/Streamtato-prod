from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_user, current_user
from werkzeug.security import generate_password_hash

from app.models import DatabaseInterface

register_bp = Blueprint('register', __name__)


@register_bp.route('/register', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('pass1')
        password2 = request.form.get('pass2')

        emailcheck = DatabaseInterface.get_user_by_email(email)
        if emailcheck:
            flash("Email already exists.", category='error')
            current_app.logger.warning(
                f"{email} was attempted to be used to create an account, but already exists.")
            return render_template("register.html", user=current_user)

        usernamecheck = DatabaseInterface.get_user_by_username(username)
        if usernamecheck:
            flash("Username already exists.", category='error')
            current_app.logger.warning(
                f"{username} was attempted to be used to create an account, but already exists.")
            return render_template("register.html", user=current_user)

        elif len(email) < 4:
            flash("Email must be greater than 4 characters.", category='error')

        elif len(username) < 2:
            flash("Username must be greater than 2 character.", category='error')

        elif password1 != password2:
            flash("Passwords don't match.", category='error')

        elif len(password1) < 7:
            flash("Password must be at least 7 characters.", category='error')

        else:
            new_user = DatabaseInterface.add_new_user(email=email, username=username, password=generate_password_hash(
                password1, method='pbkdf2:sha256'))
            login_user(new_user, remember=True)
            flash("Account created!", category='success')
            current_app.logger.info(
                f"User {username} was created.")
            return redirect(url_for('shows.shows'))

    return render_template("register.html", user=current_user)
