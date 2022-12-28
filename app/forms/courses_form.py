from app.extensions.forms import *

class CourseForm(FlaskForm):
    course = StringField('Nome do curso:')
    duration = IntegerField('Duração do curso:')
    isbttc = BooleanField('Curso BTTC', default=False)
    submit = SubmitField('Cadastrar curso')
    edit = SubmitField('Salvar alteração')

    