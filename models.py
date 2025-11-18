from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_listed = db.Column(db.Date, nullable=False)
    item_type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    images = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(100), nullable=False)
    colour = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Project {self.title}>'
