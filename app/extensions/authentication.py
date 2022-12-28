from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
login_manager = LoginManager()

def init_app(app):
    LoginManager(app)

