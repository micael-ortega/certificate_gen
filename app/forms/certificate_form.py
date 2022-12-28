from app.extensions.forms import *
from app.models import course


def choice_query():
    return course.CourseModel.query


class CertForm(FlaskForm):
    instructor = StringField('Instrutor do treinamento:')#, validators = [DataRequired()])
    course = QuerySelectField('Selecione o curso', query_factory=choice_query,
                              allow_blank=False, get_label='course', validators=[DataRequired()])
    names = TextAreaField('Nome dos participantes:')
    day_begin = DateField('Data de início:', validators=[DataRequired()])
    day_conclusion = DateField('Data de conclusão:')
    submit = SubmitField('Gerar certificados!')
