#!/usr/bin/env python3
import sqlalchemy as alc
from config import getConfig
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Table, ForeignKey, Integer, Text, Date, Float, Enum
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
UserHobbyRel = Table('UserHobbyRel', Base.metadata,
                     Column('user_id', Integer, ForeignKey('User.id')),
                     Column('hobby_id', Integer, ForeignKey('Hobby.id')))
Participation = Table('Participation', Base.metadata,
                      Column('user_id', Integer, ForeignKey('User.id')),
                      Column('event_id', Integer, ForeignKey('Event.id')))


class User(Base):
    """App user.

    Attributes:
        login: short nickname
        name: full name
        email: email address
        birthday: birthday date
        occupation: user occupation
        gender: `he`, `she` or `it`
        about: description of this user
        hobbies: list of user hobbies
        events: list of events user participating in
        passhash: hash of the password
    """
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    login = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    name = Column(Text)
    birthday = Column(Date)
    passhash = Column(Text, nullable=False)
    occupation = Column(Text)
    about = Column(Text)
    gender = Column(Enum('he', 'she', 'it', name='gender'), nullable=False)
    hobbies = relationship('Hobby', secondary=UserHobbyRel)
    events = relationship('Event', secondary=Participation)

    def set_id(self, new_id): self.id = new_id
    def set_login(self, new_login): self.login = new_login
    def set_email(self, new_email): self.email = new_email
    def set_name(self, new_name): self.name = new_name
    def set_birthday(self, new_birthday): self.birthday = new_birthday
    def set_passhash(self, new_passhash): self.passhash = new_passhash
    def set_occupation(self, new_occupation): self.occupation = new_occupation
    def set_about(self, new_about): self.about = new_about
    def set_gender(self, new_gender): self.gender = new_gender
    def set_hobbies(self, new_hobbies): self.hobbies = new_hobbies
    def set_events(self, new_events): self.events = new_events


class Hobby(Base):
    """Hobby of some users.

    Attributes:
        name: short name
        description: detailed description
        people: list of people with this hobby
    """
    __tablename__ = 'Hobby'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text)
    people = relationship('User', secondary=UserHobbyRel)


class Event(Base):
    """Event on the map.

    Attributes:
        lat: latitude
        lng: longtitude
        name: short name
        description: detailed description
        creator_id: DB id of the creator
        people: list of people participating in this event
    """
    __tablename__ = 'Event'

    id = Column(Integer, primary_key=True)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text)
    creator_id = Column(Integer, ForeignKey('User.id'))
    people = relationship('User', secondary=Participation)


def init(first_run=False):
    """Initializes ORM and gives you the Session object.

    Args:
        first_run: Is it the first run of the program. If `True` creates tables first.

    Returns:
        Session: Started session you can use for queries."""
    config = getConfig()['database']
    connect_string = 'postgresql+pypostgresql://{}:{}@{}:{}/{}'.format(config['user'],
                                                                       config['password'],
                                                                       config['host'],
                                                                       config['port'],
                                                                       config['dbname'])
    engine = alc.create_engine(connect_string)
    if first_run:
        Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    return session
