from app.extensions import database


class CourseModel(database.db.Model):

    __tablename__ = 'courses'
    
    id = database.db.Column(database.db.Integer, primary_key=True)
    course = database.db.Column(database.db.String())
    duration = database.db.Column(database.db.Integer())
    isbttc = database.db.Column(database.db.Boolean())

    def __repr__(self):
        dic = {'course': self.course,
            'duration':self.id
                }
        return '{}'.format(dic)