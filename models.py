from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_forged = db.Column(db.Date, nullable=False)
    steel_type = db.Column(db.String(100), nullable=False)
    carbon_content = db.Column(db.Float, nullable=False)
    handle_material = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    images = db.relationship('Image', backref='project', lazy=True)

    def __repr__(self):
        return f'<Project {self.title}>'


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(200), nullable=False)  # store path or URL
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign key to Project
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    def __repr__(self):
        return f'<Image {self.file_path}>'
