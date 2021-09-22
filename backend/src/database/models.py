import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_filename = "database2.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir,
                                                   database_filename))
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable
             to have multiple verisons of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    # add one demo row which helps in POSTMAN test
    group = Group(
        Teacher_name='T. Mona',
        Student_Contact_Info='[{"name": "Shahad", "color": "Shdoon@gmail.com",\
             "parts": 545101588},{"name": "Raneem", "color": "Nema@gmail.com",\
             "parts": 545154738}]'
    )
    group2 = Group(
        Teacher_name='T. Hannan ',
        Student_Contact_Info='[{"name": "Sara", "color": "Sara@gmail.com", \
            "parts": 541689754},{"name": "Lama", "color": "Lmlm@gmail.com", \
            "parts": 545658752}]'
    )
    group.insert()
    group2.insert()


'''
Group Class
    The online Qura'an recuring Group entity, extends the base SQLAlchemy Model
'''


class Group(db.Model):
    # Autoincrementing ID, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    # Group's teacher name
    Teacher_name = Column(String(80), unique=True)
    # Teachers info has the name and phone number only
    #  (is't used in the frontend yet)
    Teacher_Contact_Info = Column(String(180), nullable=True)
    # Students information (Name,Phone number, Email)
    Student_Contact_Info = Column(String(180), nullable=False)

    '''
    short()
        short form representation of the Group model
    '''

    def short(self):
        print(json.loads(self.Student_Contact_Info))
        short_recipe = [{'color': r['color'], 'parts': r['parts']}
                        for r in json.loads(self.Student_Contact_Info)]
        return {
            'id': self.id,
            'title': self.Teacher_name,
            'recipe': short_recipe
        }

    '''
    long()
        long form representation of the Group model
    '''

    def long(self):
        return {
            'id': self.id,
            'title': self.Teacher_name,
            'recipe': json.loads(self.Student_Contact_Info)
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name + unique or null ID
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model from the database
        the model must exist in the database or there'll be an error
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
    '''

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())
