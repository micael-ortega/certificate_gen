from flask import Blueprint, request, render_template, redirect, url_for

from app.forms import courses_form

from app.extensions import database
from app.extensions import authentication

from app.models import course


admin = Blueprint('admin', __name__)


@admin.route('/admin', methods=['GET', 'POST'])
@authentication.login_required
def add_course():
    form = courses_form.CourseForm()
    if request.method == 'GET':
        query = course.CourseModel.query.all()
        return render_template('admin.html', form=form, query=query)
    if request.method == 'POST':
        new_course = course.CourseModel(
            course=form.course.data, duration=form.duration.data, isbttc=form.isbttc.data)
        database.db.session.add(new_course)
        database.db.session.commit()
        query = course.CourseModel.query.all()
        return render_template('admin.html', form=form, query=query)


@admin.route('/delete/<int:id>')
@authentication.login_required
def delete_course(id):
    c = course.CourseModel.query.filter_by(id=id).first()
    database.db.session.delete(c)
    database.db.session.commit()
    return redirect(url_for('admin.add_course'))


@admin.route('/update/<int:id>', methods=['GET', 'POST'])
@authentication.login_required
def update_course(id):
    form = courses_form.CourseForm()
    if request.method == 'POST':
        edit_course = course.CourseModel.query.filter_by(id=id).first()
        edit_course.course = form.course.data
        edit_course.duration = form.duration.data
        edit_course.isbttc = form.isbttc.data
        database.db.session.commit()
        return redirect(url_for('admin.add_course'))
    else:
        query = course.CourseModel.query.filter_by(id=id).first()

        return render_template('edit.html', form=form, query=query)
