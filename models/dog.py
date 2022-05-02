from sqlalchemy.orm import relationship

from app import db

from models.park import Park

dog_parks = db.Table('dog_parks',
    db.Column('dog_id', db.ForeignKey('dogs.id'), primary_key=True),
    db.Column('park_id', db.ForeignKey('parks.id'), primary_key=True),
)


class Dog(db.Model):
    __tablename__ = 'dogs'

    id = db.Column(db.Integer, primary_key=True)
    name = db. Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=True)
    description = db.Column(db.String(), nullable=True)

    toys = relationship("Toy", backref="dog")
    parks = relationship(
        Park,
        secondary=dog_parks,
        lazy='subquery',
        backref='dogs',
    )
