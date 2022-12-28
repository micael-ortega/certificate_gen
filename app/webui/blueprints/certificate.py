from flask import Blueprint, render_template

from app.forms import certificate_form

from app.extensions import image
from app.extensions import date_conversion
from app.extensions import authentication

from datetime import date
import textwrap
import os


certificate = Blueprint('certificate', __name__)


@certificate.route('/certificate', methods=['GET', 'POST'])
@authentication.login_required
def generate_certs():

    form = certificate_form.CertForm()
    today = date.today()
    imgs = os.listdir('./webui/templates/static/img/generated')
    

    if form.validate_on_submit():
        # substituir input do formulário por opções disponíveis na db
        course = form.course.data
        day_begin = form.day_begin.data
        day_conclusion = form.day_conclusion.data
        names = form.names.data.splitlines()
        instructor = form.instructor.data

        font_name = image.ImageFont.truetype(
            "./fonts/Signature of the Ancient.ttf", size=42)
        font_text = image.ImageFont.truetype("./fonts/consola.ttf", size=24)
        font_text_small = image.ImageFont.truetype("./fonts/consola.ttf", size=18)

        if course.duration > 1:

            text_1 = f'''concluiu o treinamento "{course.course}" realizado no período de {date_conversion.convert(str(day_begin))} à {date_conversion.convert(str(day_conclusion))}, totalizando a carga horária de {course.duration} horas.
        '''

        else:
            text_1 = f'''concluiu o treinamento "{course.course}" realizado no período de {date_conversion.convert(str(day_begin))} à {date_conversion.convert(str(day_conclusion))}, totalizando a carga horária de {course.duration} hora.'''

        new_text = textwrap.fill(text=text_1, width=65)


        for name in names:
            width = 1123
            height = 794
            # fill_color_1 = '#fff'
            fill_color_1 = '#000'
            cert_name = textwrap.fill(text=name, width=50)
            # img = Image.open('./webui/templates/static/img/template12.png').date_conversion.convert('RGBA')
            img = image.Image.new("RGBA", (width, height), (255, 255, 255, 0))
            draw = image.ImageDraw.Draw(img)

            draw.text(
                (width/2, (height-620)),
                text='Certifico que',
                anchor='mm',
                align='center',
                fill=fill_color_1,
                font=font_text
            )
            # Prints student name on certificate
            draw.text(
                ((width/2), (height-550)),
                text=cert_name.title(),
                anchor='mm',
                align='center',
                fill=fill_color_1,
                font=font_name
            )
            # formated text of certificate of conclusion
            draw.text(
                (width/2, height-460),
                text=new_text,
                anchor='mm',
                align='center',
                fill=fill_color_1,
                font=font_text
            )

            draw.text(
                (width/2, height-350),
                text=f'Carmo/RJ, {date_conversion.convert(str(day_conclusion))}.',
                anchor='mm',
                align='center',
                fill=fill_color_1,
                font=font_text
            )

            # signature field below
            draw.line(
                ((width/2-200, height-200, width/2+200, height-200)),
                fill=fill_color_1,
                width=1,
            )

            draw.text(
                (width/2, height-178),
                text=f'{instructor}\nINSTRUTOR',
                anchor='mm',
                align='center',
                fill=fill_color_1,
                font=font_text_small
            )

            if course.isbttc == True:
                log = 'BTTC'
                draw.text(
                    (125, height-178),
                    text=log,
                    anchor='mm',
                    align='center',
                    fill=fill_color_1,
                    font=font_text_small
                )
            formated_name = name.replace(" ", "_").lower()
            formated_date = str(day_conclusion).replace("-", "")

            img.save(
                f"./webui/templates/static/img/generated/certificado_{formated_name}_{formated_date}.png")
            imgs = os.listdir('./webui/templates/static/img/generated')

        return render_template('end.html', imgs=imgs)

    # Deleting files in folder after user loads homepage (there must be a better way)
    for f in imgs:
        loc = './webui/templates/static/img/generated/'
        path = os.path.join(loc, f)
        print(path)
        os.remove(path)
        print(f, 'DELETED!')

    return render_template('cert_form.html', form=form, today=today)
