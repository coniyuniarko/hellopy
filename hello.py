from flask import Flask
from flask_login import LoginManager
from config import Config
from models import db, User
from user.routes import blueprint_user
from account.routes import blueprint_account

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)

# flask login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "account.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

app.register_blueprint(blueprint_user, url_prefix='/user')
app.register_blueprint(blueprint_account, url_prefix='/account')

if __name__ == "__main__":
    app.run()