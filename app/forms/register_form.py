from app.extensions import forms


class RegisterForm(forms.FlaskForm):
    name = forms.StringField('Nome completo',validators=[forms.DataRequired()])
    email = forms.EmailField('Email',validators=[forms.DataRequired()])
    password = forms.PasswordField('Senha', validators=[forms.DataRequired()])
    submit = forms.SubmitField('Registrar')

