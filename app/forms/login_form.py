from app.extensions.forms import *


class LoginForm(FlaskForm):
    email = StringField('E-mail',validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')