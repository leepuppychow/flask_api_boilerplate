from app import db 


class Toy(db.Model):
    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    name = db. Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=True)
    dog_id = db.Column(db.ForeignKey("dogs.id"))
