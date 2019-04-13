from flask_sqlalchemy import SQLAlchemy
from models import db


class Servers(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return "<uuid : {}, name : {}, description: {}>".format(self.id, self.name, self.description)
