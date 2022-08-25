from flask import Blueprint, redirect, render_template, jsonify, request, flash, url_for
from flask_login import login_required
from models import User, db
from account.libs import admin_required


blueprint_user = Blueprint(name='user', import_name=__name__, static_folder='static')

@blueprint_user.get("")
@login_required
def get_user():
    users = User.query.order_by(User.username).all()
    return render_template('user/index.html', users=users)

@blueprint_user.get("/api")
def get_api_user():
    users = User.query.order_by(User.username).all()
    json_arr = []
    for user in users:
        json_arr.append({
            "username": user.username,
            "email": user.email
        })
    return jsonify(json_arr)

@blueprint_user.post("")
@login_required
@admin_required
def post_user():
    username = request.form.get('username')
    email = request.form.get('email')
    role = request.form.get('role')
    password = request.form.get('password')
    user = User(username=username, email=email, role=role, password=password)
    db.session.add(user)
    db.session.commit()
    flash("create")
    return redirect(url_for('user.get_user'))

@blueprint_user.post("/delete")
@login_required
@admin_required
def delete_user():
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()
    flash("delete")
    return redirect(url_for('user.get_user'))
