from flask_sqlalchemy import SQLAlchemy
from flask_security import RoleMixin, UserMixin, SQLAlchemyUserDatastore, hash_password
from faker import Faker
from faker.providers import person
from sqlalchemy.orm import relationship

import random
import datetime

db = SQLAlchemy()

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    land = db.Column(db.String(100))
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('user', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    age = db.Column(db.Integer)
    email = db.Column(db.String(128), unique=True)
    username = db.Column(db.String(128), unique=True)
    land = db.Column(db.String(128))
    phone = db.Column(db.String(128))
    image_url = db.Column(db.String(256))


def seed_data():
    if not Role.query.first():
        user_datastore.create_role(name='Admin')
        user_datastore.create_role(name='User')
        db.session.commit()

    if not User.query.first():
        user_datastore.create_user(email='test@example.com', password=hash_password('password'), roles=['Admin', 'User'],
                                   confirmed_at=datetime.datetime.now())
        user_datastore.create_user(email='random@mail.com', password=hash_password('password'), roles=['User'],
                                   confirmed_at=datetime.datetime.now())
        user_datastore.create_user(email='sergey@mail.com', password=hash_password('password'), roles=['Admin'],
                                   confirmed_at=datetime.datetime.now())
        db.session.commit()

    faker = Faker()
    faker.add_provider(person)

    while Person.query.count() < 100:
        new_name = faker.name()
        new_age = random.randint(18, 60)
        new_email = faker.email()
        new_country = faker.country()
        new_username = faker.user_name()
        fake_image_url = faker.image_url(width=200, height=200)  
        new_phone = str(random.randint(10000000, 99999999))

        new_user = Person(name=new_name, age=new_age, email=new_email, username=new_username, phone=new_phone,
                          land=new_country, image_url=fake_image_url)
        db.session.add(new_user)
        db.session.commit()


