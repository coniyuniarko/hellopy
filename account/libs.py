from functools import wraps
from flask_login import current_user
from flask import redirect


def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.role == "ADMIN":
            return f(*args, **kwargs)
        else:
            return redirect('/login')
    return wrap

