from app import db


class SampleModel(db.Model):
    __tablename__ = 'samples'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
