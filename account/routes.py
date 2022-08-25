from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_user, login_required, logout_user
from models import User


blueprint_account = Blueprint(name='account', import_name=__name__, static_folder='static')

@blueprint_account.get("/login")
def login():
    return render_template('account/login.html')

@blueprint_account.post("/login")
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    if user and user.is_password_valid(password):
        login_user(user, remember=remember)
        next = request.args.get('next')
        if next:
            return redirect(next)
        return redirect(url_for('user.get_user'))
    return redirect(url_for('account.login'))

@blueprint_account.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('account.login'))
