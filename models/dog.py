from sqlalchemy.orm import relationship

from app import db


class Dog(db.Model):
    __tablename__ = 'dogs'

    id = db.Column(db.Integer, primary_key=True)
    name = db. Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=True)
    description = db.Column(db.String(), nullable=True)

    toys = relationship("Toy", backref="dog")
