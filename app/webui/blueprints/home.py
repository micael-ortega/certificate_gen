from flask import Blueprint, render_template, redirect, request, url_for

from app.forms import login_form
from app.forms import register_form

from app.extensions import database
from app.extensions import authentication

from app.models import users


home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
@home.route('/login', methods=['GET', 'POST'])
def login():
    form = login_form.LoginForm()

    if request.method == 'POST':
        email = form.email.data
        pwd = form.password.data

        user = users.Users.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('home.login'))

        authentication.login_user(user)
        return redirect(url_for('certificate.generate_certs'))

    return render_template('home.html', form=form)


@home.route('/register', methods=['GET', 'POST'])
@authentication.login_required
def register():
    form = register_form.RegisterForm()

    if request.method == 'POST':
        name = form.name.data
        email = form.email.data
        pwd = form.password.data

        if name and email and pwd:
            user = users.Users(name=name, email=email, password=pwd)
            database.db.session.add(user)
            database.db.session.commit()

        return redirect(url_for('home.login'))

    return render_template('register_form.html', form=form)


@home.route('/logout')
def logout():
    
    authentication.logout_user()
    return redirect(url_for('home.login'))
