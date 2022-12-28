from flask import Flask

from app.extensions import database
from app.extensions import authentication

from app.webui.blueprints.certificate import certificate
from app.webui.blueprints.admin import admin
from app.webui.blueprints.home import home


def create_app():

    app = Flask(__name__, template_folder='./webui/templates',
                static_folder='./webui/templates/static/')

    
    app.config['SECRET_KEY'] = 'my-secret'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.sqlite3"


   

    with app.app_context():
        database.db.init_app(app)
        database.db.create_all()

    authentication.login_manager.init_app(app)

    app.register_blueprint(home)
    app.register_blueprint(certificate)
    app.register_blueprint(admin)

    return app
