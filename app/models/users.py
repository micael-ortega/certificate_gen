from app.extensions import database
from app.extensions import authentication
from werkzeug.security import generate_password_hash, check_password_hash


@authentication.login_manager.user_loader
def load_user(user_id):
    return Users.query.filter_by(id=user_id).first()

class Users(database.db.Model, authentication.UserMixin):
    __tablename__ = 'users'
    id = database.db.Column(database.db.Integer, primary_key=True, autoincrement=True)
    name = database.db.Column(database.db.String(86), nullable=False)
    email = database.db.Column(database.db.String(84), nullable=False, unique=True)
    password = database.db.Column(database.db.String(128), nullable=False)
    #isadmin = database.db.Column(database.db.Boolean, nullable=False)

    def __init__(self, name, email, password, isadmin):
        self.name = name
        self.email = email
        #self.isadmin = isadmin
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

